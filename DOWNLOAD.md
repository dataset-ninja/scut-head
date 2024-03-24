Dataset **Scut Head** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/n/s/AI/ulFoMo1hd4P3ZJvgOKgEwjFKMKRJ7sRPCv1BX0AkAKWsG7vEDINDa9hYmHHEpcpEaNBaESYkXHJjy8HekFKeR7qNBRp0eh4xU54qmQwiFb7dMK8LZbwnbTt2NmFr.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Scut Head', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be downloaded here:

- [PartA of SCUT-HEAD](https://drive.google.com/open?id=1yaOF9os5wPVNNG4GVzNyULLVe74vdrBE)
- [PartB of SCUT-HEAD](https://drive.google.com/open?id=1LZ_KlTPStDEcqycfqUkDkqQ-aNMMC3cl)
