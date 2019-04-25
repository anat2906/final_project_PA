const path = require("path"),
  gulp = require("gulp"),
  minify = require("gulp-minify"),
  prefixer = require("gulp-autoprefixer"),
  cssmin = require("gulp-minify-css"),
  sass = require("gulp-sass"),
  rigger = require("gulp-rigger"),
  plumber = require("gulp-plumber"),
  notify = require("gulp-notify"),
  concat = require("gulp-concat"),
  jsmin = require("gulp-jsmin"),
  imagemin = require("gulp-imagemin"),
  pngquant = require("imagemin-pngquant"),
  jpegtran = require("imagemin-jpegtran"),
  gifsicle = require("imagemin-gifsicle"),
  optipng = require("imagemin-optipng"),
  iconfont = require("gulp-iconfont"),
  iconfontCss = require("gulp-iconfont-css"),
  sourcemaps = require("gulp-sourcemaps"),
  runTimestamp = Math.round(Date.now() / 1000);

var paths = {
  src: {
    js: "static/js/",
    style: "static/sass/style.scss",
    img: "static/img//*.*",
    uploads: "static/uploads//*.*",
    fonts: "static/fonts//*.*",
    html: "static/html/*.*"
  },
  build: {
    js: "static/build/js/",
    css: "static/build/css/",
    img: "static/build/img/",
    uploads: "static/build/uploads/",
    fonts: "static/build/fonts/",
    html: "static/build/html/"
  },
  watch: {
    js: "static/js//*.js",
    style: "static/sass//*.*",
    img: "static/img//*.*",
    uploads: "static/uploads//*.*",
    html: "static/html//*.*"
  }
};

gulp.task("build:js", function() {
  return gulp
    .src([
      "static/vendor/jquery/dist/jquery.js",
      "static/vendor/tether-master/dist/js/tether.js",
      "static/vendor/bootstrap/js/dist/util.js",
      "static/vendor/bootstrap/js/dist/modal.js",
      "static/vendor/bootstrap/js/dist/tab.js",
      "static/vendor/bootstrap/js/dist/collapse.js",
      "static/vendor/device.js/lib/device.js",
      "static/vendor/swiper/dist/js/swiper.js",
      "static/vendor/Inputmask/dist/jquery.inputmask.bundle.js",
      "static/vendor/jquery-validation/dist/jquery.validate.js",
      "static/vendor/autosize/dist/autosize.js",
      "static/vendor/photoswipe/dist/photoswipe.js",
      "static/vendor/mixitup/dist/mixitup.js",
      "static/vendor/photoswipe/dist/photoswipe-ui-default.js",
      "static/vendor/jquery_appear/jquery.appear.js",
      path.join(paths.src.js, "validate.js"),
      path.join(paths.src.js, "main.js")
    ])
    .pipe(sourcemaps.init())
    .pipe(concat("main.js"))
    .pipe(rigger())
    .pipe(jsmin())
    .pipe(sourcemaps.write("./maps"))
    .pipe(gulp.dest(paths.build.js));
});

gulp.task("build:scss", function() {
  gulp
    .src(paths.src.style)
    .pipe(
      plumber({
        errorHandler: notify.onError(function(err) {
          return {
            title: "Error SASS",
            message: err.message
          };
        })
      })
    )
    .pipe(sourcemaps.init())
    .pipe(sass().on("error", sass.logError))
    .pipe(sourcemaps.write())
    .pipe(prefixer("last 20 versions"))
    .pipe(cssmin())
    .pipe(gulp.dest(paths.build.css));
});
gulp.task("build:icon", function() {
  return gulp
    .src("static/img/icons//*.*")
    .pipe(
      iconfontCss({
        fontName: "icon",
        cssClass: "icon",
        path: "static/fonts/icon/template.scss",
        targetPath: "icons.scss",
        fontPath: "/static/build/fonts/icons/"
      })
    )
    .pipe(
      iconfont({
        fontName: "icon",
        prependUnicode: true,

        appendCodepoints: true,
        appendUnicode: false,
        normalize: true,
        fontHeight: 1000,

        formats: ["svg", "ttf", "eot", "woff", "woff2"],
        timestamp: runTimestamp
      })
    )
    .on("glyphs", function(glyphs, options) {
      // CSS templating, e.g.
      console.log(glyphs, options);
    })
    .pipe(gulp.dest(path.join(paths.build.fonts, "icons")));
});

gulp.task("build:fonts", function() {
  return gulp
    .src([paths.src.fonts, "static/vendor/font-awesome/fonts//*.*"])
    .pipe(gulp.dest(paths.build.fonts));
});
gulp.task("build:img", function() {
  gulp
    .src(paths.src.img)
    .pipe(
      imagemin({
        progressive: true,
        svgoPlugins: [
          {
            removeViewBox: false
          }
        ],
        use: [pngquant(), jpegtran(), optipng(), gifsicle()]
      })
    )
    .pipe(gulp.dest(paths.build.img));
});

gulp.task("build", [
  "build:icon",
  "build:fonts",
  "build:js",
  "build:img",
  "build:scss"
]);

gulp.task("watch:js", function() {
  gulp.watch([paths.watch.js], function(event, cb) {
    gulp.start("build:js");
  });
});

gulp.task("watch:style", function() {
  gulp.watch([paths.watch.style], function(event, cb) {
    gulp.start("build:scss");
  });
});

gulp.task("watch:html", function() {
  gulp.watch([paths.watch.html], function(event, cb) {
    gulp.start("build:html");
  });
});
