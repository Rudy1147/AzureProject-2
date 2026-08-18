// Passed as --parameters paramName=value paramName2=value2
param resourceGroupLocation string
param storageAccountName    string

// Storage account for files. See:
// https://learn.microsoft.com/en-us/azure/templates/microsoft.storage/storageaccounts?pivots=deployment-language-bicep
resource p2SA 'Microsoft.Storage/storageAccounts@2021-09-01' = {
    name: storageAccountName
    location: resourceGroupLocation
    sku: {
        name: 'Standard_LRS'
    }
    kind: 'StorageV2'
    properties: {
        accessTier: 'Hot'
    }
}

// Setup needed to configure containers. See:
// https://github.com/Azure/azure-quickstart-templates/blob/master/quickstarts/microsoft.storage/storage-multi-blob-container/main.bicep
resource blobServices 'Microsoft.Storage/storageAccounts/blobServices@2023-01-01' = {
  parent: p2SA
  name: 'default'
}

// The general structure should look like:
// <STORAGEACCOUNT>/<CONTAINER>user-job-files/andrew-bates/job1/input/someimage.png
resource container 'Microsoft.Storage/storageAccounts/blobServices/containers@2023-01-01' = {
    parent: blobServices
    name: 'user-job-files'
}

// TODO: Add RBAC for webservices and functions, so that files can be uploaded 
// and viewed from within the storage account.
