module.exports = {
  devServer: {
    hot: true,
    publicPath: '/',
    proxy: {
      '/': {
        target: 'http://192.168.0.107:8000/',
        secure: false,
        changeOrigin: true,
      }
    },
  },
  configureWebpack: {
    devtool: 'source-map',
  },
};