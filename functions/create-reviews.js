function main(params) {
    return new Promise(function (resolve, reject) {
      const { CloudantV1 } = require("@ibm-cloud/cloudant");
      const { IamAuthenticator } = require("ibm-cloud-sdk-core");
      const authenticator = new IamAuthenticator({
        apikey: "",
      });
      const cloudant = CloudantV1.newInstance({
        authenticator: authenticator,
      });
      cloudant.setServiceUrl("");
      // Add Id to review
      doc = params.review;
      doc.id = Math.floor(Math.random() * (80 - 15) + 15);
      cloudant
        .postDocument({
          db: "reviews",
          document: doc,
        })
        .then((result) => {
          let code = 201;
          resolve({
            statusCode: code,
            headers: { "Content-Type": "application/json" },
          });
        })
        .catch((err) => {
          reject(err);
        });
    });
  }
