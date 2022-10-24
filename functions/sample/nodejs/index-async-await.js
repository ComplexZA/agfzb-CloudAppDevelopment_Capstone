/**
 * Get all dealerships
 */

const { CloudantV1 } = require('@ibm-cloud/cloudant');
const { IamAuthenticator } = require('ibm-cloud-sdk-core');

async function main(params) {
    let databaseName = "dealerships"
    const client = Cloudant({
        url: params.COUCH_URL,
        plugins: { iamauth: { iamApiKey: params.IAM_API_KEY } }
    });

    try {
        let db = client.db.use(databaseName);
        let dbList = await client.db.list();
        console.log(dbList);
        return { "dbs": dbList };
    } catch (error) {
        return { error: error.description };
    }
}
