var window_width = 800;
var window_height = 600;
var frame_rate = 30;
var inter_frame_interval = (1.0/frame_rate);

var good_idea_count = 5;
var bad_idea_count = 10;

var engines_firing = false;

function game_object() {};

function idea() {};
idea.prototype = new game_object;

function good_idea() {};
good_idea.prototype = new idea;

function bad_idea(){};
bad_idea.prototype = new idea;

function player() {};
player.prototype = new game_object;

player.prototype.











