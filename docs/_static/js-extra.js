function goto_prev() {
  var prev_section = null;
  $('.section').each(function() {
    var section = $(this);
    var position = section.position().top - $(window).scrollTop();
    if (position < 0) { // before bottom of navbar
      prev_section = section;
    }
  });
  if (prev_section != null) {
    window.scrollTo(0, prev_section.position().top);
  } else {
    goto_top();
  }
}

function goto_top() {
  window.scrollTo(0, 0);
}

function goto_next() {
  var next_section = null;
  $('.section').each(function() {
    var section = $(this);
    var position = section.position().top - $(window).scrollTop();
    if (next_section == null && position > 1) {
      next_section = section;
    }
  });
  if (next_section != null) {
    window.scrollTo(0, next_section.position().top);
  } else {
    goto_bottom();
  }
}

function goto_bottom() {
  window.scrollTo(0, $('.document').height());
}

$(document).keydown(function(event) {
  if (event.keyCode == 37 || event.keyCode == 80) {
    goto_prev();
  } else if (event.keyCode == 39 || event.keyCode == 78) {
    goto_next();
  } else if (event.keyCode == 84) {
    goto_top();
  } else if (event.keyCode == 66) {
    goto_bottom();
  }
});
