module.exports = {
  "assetsDir": "../static/emanagement",
  "indexPath": "../templates/emanagement/index.html",
  "filenameHashing": false,
  "configureWebpack": {
    "performance": {
      "hints": false
    },
    "optimization": {
      "splitChunks": {
        "minSize": 10000,
        "maxSize": 250000
      }
    }
  },
  "transpileDependencies": [
    "vuetify"
  ]
}