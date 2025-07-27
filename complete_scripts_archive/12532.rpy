label avg12532:

play music "ed7513.ogg"
scene avg_bg_023
$ update_portrait('sc007_01 1', 'p15', [l(-17), light, flip], 6)
$ update_narrator('c151')
window show
with fade_in
c151 '[convertstrid(1151665)]'
$ update_portrait('sc007_01 1', 'p15', [l(-17), dark, flip], 6)
$ update_portrait('sc028_01 1', 'p36', [r(-7), light], 5)
c363 '[convertstrid(1151666)]'
hide p15
$ update_portrait('sc028_01 1', 'p36', [r(-7), dark], 5)
$ update_portrait('sc008_01 1', 'p16', [l(-18), light, flip], 6)
c161 '[convertstrid(1151667)]'
hide p16
$ update_portrait('sc007_01 1', 'p15', [l(-17), light, flip], 6)
c151 '[convertstrid(1151668)]'
$ update_portrait('sc007_01 1', 'p15', [l(-17), dark, flip], 6)
$ update_portrait('sc028_01 1', 'p36', [r(-7), light], 5)
c363 '[convertstrid(1151669)]'
$ update_portrait('sc028_01 1', 'p36', [r(-7), dark], 5)
$ update_portrait('sc007_01 1', 'p15', [l(-17), l_shake, light, flip], 6)
c151 '[convertstrid(1151670)]'
hide p15
hide p36
$ update_narrator('c12021')
with fade
c12021 '[convertstrid(1151671)]'
$ update_portrait('oc007_01 1', 'p7', [r(-24), light], 5)
c73 '[convertstrid(1151672)]'
hide p7
$ update_portrait('st041_01 4', 'p240', [r(-1), light], 5)
c2403 '[convertstrid(1151673)]'
$ update_portrait('st041_01 4', 'p240', [r(-1), dark], 5)
$ update_portrait('oc007_01 1', 'p7', [l(-24), light, flip], 6)
c71 '[convertstrid(1151674)]'
$ update_portrait('oc007_01 1', 'p7', [l(-24), dark, flip], 6)
$ update_portrait('st041_01 3', 'p240', [r(-1), light], 5)
c2403 '[convertstrid(1151675)]'
hide p7
hide p240
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 5)
$ update_narrator('c43')
with fade
c43 '[convertstrid(1151676)]'
$ update_portrait('oc004_01 8', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1151677)]'
hide p3
$ update_portrait('sc005_01 4', 'p13', [l_entrance(-17), light, flip], 6)
c131 '[convertstrid(1151678)]'
hide p4
$ update_portrait('sc005_01 4', 'p13', [l(-17), dark, flip], 6)
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 5)
c23 '[convertstrid(1151679)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na04_b.ogg"
c13 '[convertstrid(1151680)]'
return