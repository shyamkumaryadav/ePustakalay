const path = require("path");


module.exports = {
  "outputDir": path.resolve(__dirname, "../backend/emanagement"),
  "assetsDir": "static/emanagement",
  "indexPath": "templates/emanagement/index.html",
  "transpileDependencies": [
    "vuetify"
  ]
}