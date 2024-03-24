The authors have collected and labeled a new large **Scut Head Dataset** which includes 4405 images with 111251 heads annotated. The dataset consists of two parts. ***part a*** includes 2000 images sampled from monitor videos of classrooms in an university with 67321 heads annotated. ***part b*** includes 2405 images crawled from internet with 43930 heads annotated. They have labelled every visable heads with xmin, ymin, xmax and ymax coordinates and ensured that annotations cover the entire head including the blocked parts but without extra background. Both ***part a*** and ***part b*** are divided into training and testing parts.

## Motivation

Face detection and pedestrian detection represent pivotal challenges in the field of computer vision, and notable advancements have been made in recent years. However, practical applications reveal certain limitations. For instance, face detection algorithms are restricted to identifying frontal faces, rendering individuals facing away from the camera undetectable. Similarly, in complex indoor environments, where body parts may be obscured, pedestrian detection encounters difficulties. Head detection, on the other hand, presents fewer limitations and proves more adept at locating and enumerating individuals, particularly in indoor settings. Nevertheless, detecting heads indoors poses its own set of challenges, including variations in scale and appearance, as well as the task of identifying smaller heads. Addressing these challenges necessitates effective exploitation of extracted features to accurately localize heads and discern them from the background—a formidable task. Prior approaches have often relied on leveraging multi-scale features derived from different layers of deep convolutional neural networks to tackle these complexities.

Detecting small heads presents a distinct challenge in head detection tasks. To address this, the authors have introduced a cascaded multi-scale architecture tailored specifically for small head detection. Their approach centers on refining local detection outcomes by enhancing the resolution of image segments. The proposed architecture comprises two distinct detectors: a global detector and a local detector. The global detector is tasked with identifying large heads and subsequently relays this information to the local detector, which then focuses on analyzing enlarged segments containing small heads for more precise detection. Additionally, owing to the scarcity of datasets dedicated to head detection, the authors have curated and annotated a large-scale dataset specifically for this purpose, named SCUT-HEAD.

## Dataset description

The authors have curated and annotated a comprehensive head detection dataset named SCUT-HEAD, which comprises two distinct parts. ***part a*** consists of 2000 images extracted from surveillance videos captured in university classrooms, encompassing a total of 67,321 annotated heads. To ensure dataset diversity and reduce similarity, representative images were thoughtfully selected, considering the inherent similarities across classroom settings. 

<img src="https://github.com/dataset-ninja/scut-head/assets/120389559/479478e6-a971-4492-8520-d7059da7364a" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">An example image and annotations of Part A in SCUT-HEAD.</span>

On the other hand, ***part b*** consists of 2405 images sourced from the internet, with 43,930 annotated heads. Each visible head in both ***part a*** and ***part b*** is meticulously labeled with coordinates (xmin, ymin, xmax, ymax), encompassing the entire head region while excluding any extraneous background. 

<img src="https://github.com/dataset-ninja/scut-head/assets/120389559/73b815a1-4dda-4797-a31f-a05086b52c10" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">An example image and annotations of Part B in SCUT-HEAD.</span>

Both ***part a*** and ***part b*** are further divided into training and testing subsets. Specifically, ***part a*** includes 1500 images for training and 500 for testing, while ***part b*** comprises 1905 training images and 500 testing images. 

