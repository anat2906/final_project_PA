'use strict';

const path = require('path');
const gulp = require('gulp');
const sass = require('gulp-sass');
 
const paths = {
  src: {
      style: './sass/**/style.scss'
  },
  build: {
      css: './static/css/'
  },
  watch: {
      style: './sass/**/*.*',
  }
};

gulp.task('sass', function () {
  return gulp.src(paths.src.style)
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest(paths.build.css));
});

 
gulp.task('sass:watch', function () {
  gulp.watch([paths.watch.style], gulp.parallel("sass"));
});
