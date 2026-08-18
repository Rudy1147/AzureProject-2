// Needed to create a new resource group, otherwise we'd need to target an
// existing resource group.
targetScope='subscription'

// Passed as --parameters paramName=value paramName2=value2
param projectName           string
param resourceGroupLocation string
param deploymentEnviroment  string
param storageAccountName    string = 'sajobfiles${uniqueString(newGuid())}'

// Create/update project 2's resource group, using the API passed as a string.
resource p2RG 'Microsoft.Resources/resourceGroups@2026-06-01' = {
    name:     'rg-${projectName}-${deploymentEnviroment}'
    location: resourceGroupLocation
}

// Storage account for job input/output files, which is defined in the passed
// bicep file.
module p2SAModule './storage.bicep' = {
    name: 'deployStorage'
    scope: p2RG
    params: {
        resourceGroupLocation: resourceGroupLocation
        storageAccountName: storageAccountName
    }
}
