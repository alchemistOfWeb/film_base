import path from "./gulpconfig/path.js";

import gulp from "gulp";
import browserSync from "browser-sync";

// import pug from "./gulptasks/pug.js";
import clear from "./gulptasks/clear.js";
import scss from "./gulptasks/scss.js";
import js from "./gulptasks/js.js";
import img from "./gulptasks/img.js";
import icon from "./gulptasks/icon.js";
import font from "./gulptasks/font.js";
import app from "./config/app.js";


const watcher = () => {
    // does it works or need to use browserSync.create()?
    // gulp.watch(path.pug.watch, pug).on("all", browserSync.reload);
    gulp.watch(path.scss.watch, scss).on("all", browserSync.reload);
    gulp.watch(path.js.watch, js).on("all", browserSync.reload);
    gulp.watch(path.img.watch, img).on("all", browserSync.reload);
    gulp.watch(path.icon.watch, icon).on("all", browserSync.reload);
    gulp.watch(path.font.watch, font).on("all", browserSync.reload);
};

const server = () => {
    browserSync.init({
        server: {
            baseDir: path.root
        }
    })
}

const build = gulp.series(
    clear,
    gulp.parallel(scss, js, font, icon, img)
);

const dev = gulp.series(
    build,
    gulp.parallel(watcher, server)
);

export { scss, js, img, icon, font, watcher, clear }
export default app.isProd ? build : dev;
