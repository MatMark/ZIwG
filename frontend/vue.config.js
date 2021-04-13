const CompressionPlugin = require("compression-webpack-plugin");

module.exports = {
  transpileDependencies: ["vuetify"],
  devServer: {
    public: "matmark.ddns.net",
    host: "0.0.0.0",
    disableHostCheck: true
  },
  configureWebpack: {},
  chainWebpack(config) {
    config.plugins.delete("prefetch");
    config.plugin("CompressionPlugin").use(CompressionPlugin);
  }
};
