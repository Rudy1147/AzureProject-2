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
