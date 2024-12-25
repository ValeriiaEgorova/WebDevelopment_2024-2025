const gulp = require('gulp');
const rename = require('gulp-rename');
const fs = require('fs');
const path = require('path');
const browserSync = require('browser-sync').create();

// Путь к файлам
const paths = {
    html: './*.html',
    css: './css/**/*.css',
    js: './js/**/*.js',
    dist: 'dist/**/*.*',
    distDir: 'dist'
};


// Задача: добавление даты к именам файлов в папке dist
gulp.task('rename-files', function () {
    const date = new Date().toISOString().split('T')[0];
    return gulp.src(paths.dist)
        .pipe(rename(function (file) {
            file.basename += `-${date}`;
        }))
        .pipe(gulp.dest(paths.distDir));
});

// Задача: создание файла system-info.txt в папке dist
gulp.task('system-info', function (done) {
    const info = `OS: ${process.platform}\nDate: ${new Date().toLocaleString()}`;
    fs.writeFileSync(path.join(paths.distDir, 'system-info.txt'), info);
    done();
});

// Задача: запуск локального сервера
gulp.task('serve', function (cb) {
    browserSync.init({
        server: {
            baseDir: './'
        },
        notify: false,
        open: true
    });
    cb();
});

// Задача: перезагрузка браузера
gulp.task('reload', function (cb) {
    browserSync.reload();
    cb();
});

// Задача: наблюдение за файлами
gulp.task('watch-files', function () {
    gulp.watch(paths.html, gulp.series('reload'));
    gulp.watch(paths.css, gulp.series('reload'));
    gulp.watch(paths.js, gulp.series('reload'));
});

// Задача: последовательное выполнение rename-files и system-info
gulp.task('sequential', gulp.series('rename-files', 'system-info'));

// Задача: параллельное выполнение rename-files и system-info
gulp.task('parallel', gulp.parallel('rename-files', 'system-info'));

// Задача по умолчанию: запуск сервера и наблюдение за файлами
gulp.task('default', gulp.series('serve', 'watch-files'));
