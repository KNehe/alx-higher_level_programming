$(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (res, status) {
    if (status === 'success') {
      $('#hello').text(res.hello);
    }
  });
});
