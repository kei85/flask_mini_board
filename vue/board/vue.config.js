module.exports = {
  devServer: {
      proxy: {
          "/api": {
              target: "http://flask:5000",
          },
      },
  },
}