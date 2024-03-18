import os
import shutil
import xml.etree.ElementTree as ET

import supervisely as sly
from dataset_tools.convert import unpack_if_archive
from supervisely.io.fs import (
    file_exists,
    get_file_name,
    get_file_name_with_ext,
    get_file_size,
)
from tqdm import tqdm

import src.settings as s


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    # Possible structure for bbox case. Feel free to modify as you needs.

    a_split_path = "/home/alex/DATASETS/TODO/SCUT-HEAD/SCUT_HEAD_Part_A/ImageSets/Main"
    b_split_path = "/home/alex/DATASETS/TODO/SCUT-HEAD/SCUT_HEAD_Part_B/ImageSets/Main"
    a_images_path = "/home/alex/DATASETS/TODO/SCUT-HEAD/SCUT_HEAD_Part_A/JPEGImages"
    b_images_path = "/home/alex/DATASETS/TODO/SCUT-HEAD/SCUT_HEAD_Part_B/JPEGImages"
    batch_size = 30
    ds_name = "ds"
    bboxes_ext = ".xml"

    def create_ann(image_path):
        labels = []

        if get_file_name(image_path)[4] == "A":
            tag = sly.Tag(part1_meta)
        else:
            tag = sly.Tag(part2_meta)

        ann_path = image_path.replace("JPEGImages", "Annotations").replace(".jpg", ".xml")

        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]

        if file_exists(ann_path):
            tree = ET.parse(ann_path)
            root = tree.getroot()

            all_objects = root.findall(".//object")

            for curr_object in all_objects:
                coords_xml = curr_object.findall(".//bndbox")
                for curr_coord in coords_xml:
                    left = int(curr_coord[0].text)
                    top = int(curr_coord[1].text)
                    right = int(curr_coord[2].text)
                    bottom = int(curr_coord[3].text)

                    if get_file_name(image_path) == "PartB_01015":
                        a = 0

                    if top < bottom and left < right:
                        rect = sly.Rectangle(left=left, top=top, right=right, bottom=bottom)
                        label = sly.Label(rect, obj_class)
                        labels.append(label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels, img_tags=[tag])

    obj_class = sly.ObjClass("person", sly.Rectangle, color=(255, 0, 0))
    part1_meta = sly.TagMeta("part a", sly.TagValueType.NONE)
    part2_meta = sly.TagMeta("part b", sly.TagValueType.NONE)

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=[obj_class], tag_metas=[part1_meta, part2_meta])
    api.project.update_meta(project.id, meta.to_json())

    for ds_name in ["train", "val", "test"]:
        dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

        curr_pathes = []
        curr_a_split_path = os.path.join(a_split_path, ds_name + ".txt")
        with open(curr_a_split_path) as f:
            content = f.read().split("\n")
            for name in content:
                if len(name) > 0:
                    curr_pathes.append(os.path.join(a_images_path, name + ".jpg"))

        curr_b_split_path = os.path.join(b_split_path, ds_name + ".txt")
        with open(curr_b_split_path) as f:
            content = f.read().split("\n")
            for name in content:
                if len(name) > 0:
                    curr_pathes.append(os.path.join(b_images_path, name + ".jpg"))

        progress = sly.Progress("Create dataset {}".format(ds_name), len(curr_pathes))

        for img_pathes_batch in sly.batched(curr_pathes, batch_size=batch_size):
            images_names_batch = [
                get_file_name_with_ext(image_path) for image_path in img_pathes_batch
            ]

            img_infos = api.image.upload_paths(dataset.id, images_names_batch, img_pathes_batch)
            img_ids = [im_info.id for im_info in img_infos]

            anns = [create_ann(image_path) for image_path in img_pathes_batch]
            api.annotation.upload_anns(img_ids, anns)

            progress.iters_done_report(len(images_names_batch))

    return project
