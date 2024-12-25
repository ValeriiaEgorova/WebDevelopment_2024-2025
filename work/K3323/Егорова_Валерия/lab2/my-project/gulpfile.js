const gulp = require('gulp');

function copyFiles() {
  return gulp.src('src/*')
    .pipe(gulp.dest('dist'));
}

exports.default = copyFiles;
