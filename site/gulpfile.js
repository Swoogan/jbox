var cssnano = require('gulp-cssnano');
var gulp = require('gulp');
var rename = require('gulp-rename');
var uglify = require('gulp-uglify');
var usemin = require('gulp-usemin');

gulp.task('default', function() {
    gulp.src('./app.src.html')
        .pipe(rename('app.html'))
        .pipe(gulp.dest('./'));
});

gulp.task('minify', function() {
    gulp.src('./app.src.html')
        .pipe(rename('app.html'))
        .pipe(usemin({
            assetsDir: '.',
            css: [cssnano(), 'concat'],
            js: [uglify(), 'concat']
        }))
        .pipe(gulp.dest('./'));
});
