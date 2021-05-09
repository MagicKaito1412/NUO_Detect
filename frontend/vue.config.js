module.exports = {
    devServer: {
        port: 8000
    },
    css: {
        loaderOptions: {
            sass: {
                additionalData: `
                @import "@/assets/scss/colors.scss";
                `
            }
        }
    },
    runtimeCompiler: true
};
