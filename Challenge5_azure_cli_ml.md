Login

```
az login
```

Configure 

```
az provider register -n Microsoft.MachineLearningComputen
az provider register -n Microsoft.ContainerServicen
az provider register -n Microsoft.ContainerRegistry

az provider show -n Microsoft.ContainerServicerope
az provider show -n Microsoft.MachineLearningComputen
az provider show -n Microsoft.ContainerRegistry
```

Create model management account

```
az ml account modelmanagement set -n happymodelmgmt -g anatoliy2
```

Create new env

```bash
az ml env setup -l "West Europe" -n localenv -g anatoliy2
```


Inspect status of env

```bash
az ml env show -g anatoliy2 -n localenv
```


Set env

```bash
az ml env set -g anatoliy2 -n localenv
```


Register model

```
az ml model register --model model.h5 --name keras.registered.model
```

View logs
```
az ml service logs realtime -i localwebservice3
```

Create manifest

```bash
anatoliy@anatoliydl:~$ az ml manifest create --manifest-name test_manifest4 --model-id 73f1b7ee8f334e04b2b93cfad27a221d -r python -p ./dependencies.txt  -f source.py -s outputs/schema.json

```

Create docker image

```bash
az ml image create -n testimage4 --manifest-id fbb2e23c-552b-4399-963c-2264fb6cae16
```

Create web service

```bash
az ml service create realtime --image-id 2905a585-2d78-42b3-beb5-6645e72ebc46 -n localwebservice4
```

Test

```bash
anatoliy@anatoliydl:~$ az ml service run realtime -i localwebservice4 -d "{\"doc_base64\": \"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\"}"
```

Logout

```bash
az logout
```

