// progressbar.js@1.0.0 version is used
// Docs: http://progressbarjs.readthedocs.org/en/1.0.0/
var r = document.getElementById('a')
var say = Number(r.value) / 5 + 0.2

var bar = new ProgressBar.Path('#heart-path', {
  easing: 'easeInOut',
  duration: 1400
});

bar.set(0);
bar.animate(say);  // Number from 0.0 to 1.0

var r2 = document.getElementById('b')
var say2 = Number(r2.value) / 5 + 0.2

var bar2 = new ProgressBar.Path('#heart-path2', {
  easing: 'easeInOut',
  duration: 1400
});

bar2.set(0);
bar2.animate(say2);  // Number from 0.0 to 1.0
