label avg20099:
stop music

play music "ed7104.ogg"
scene avg_bg_037
window show
with fade_in
play sfx2 "other_7064.ogg"
c6831 '[textdict[1004837]]'
c6843 '[textdict[1004838]]'
c6831 '[textdict[1004839]]'
c6843 '[textdict[1004840]]'
c6831 '[textdict[1004841]]'
c6831 '[textdict[1004842]]'
c6853 '[textdict[1004843]]'
c6861 '[textdict[1004844]]'
c6853 '[textdict[1004845]]'
c6861 '[textdict[1004846]]'
c6853 '[textdict[1004847]]'
$ update_portrait('oc001_01 1', 'p1', [l_entrance(-2), light, flip], 6)
play sfxvoice "avg_vocal_na15.ogg"
c11 '[textdict[1004848]]'
hide p1
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('sc039_01 1', 'p46', [r(-13), light], 5)
c463 '[textdict[1004849]]'
return