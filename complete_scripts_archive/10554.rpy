label avg10554:

$ play_music("ED6102.ogg")
scene avg_bg_106
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(1153714)]'
$ update_portrait('sc031_01 5', 'p39', [l(-14), light, flip], 6)
c391 '[convertstrid(1153715)]'
$ update_portrait('sc031_01 5', 'p39', [l(-14), dark, flip], 5)
$ update_portrait('sc030_01 4', 'p38', [r(-12), light], 6)
c383 '[convertstrid(1153716)]'
hide p38
$ update_portrait('oc002_01 8', 'p2', [r_entrance(-3), light], 6)
c23 '[convertstrid(1153717)]'
hide p39
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('sc032_01 1', 'p40', [l(-17), light, flip], 6)
c401 '[convertstrid(1153718)]'
$ update_portrait('sc032_01 1', 'p40', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch04_b.ogg"
c23 '[convertstrid(1153719)]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [r_entrance(-2), light], 6)
c13 '[convertstrid(1153720)]'
hide p40
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc031_01 5', 'p39', [l(-14), light, flip], 6)
c391 '[convertstrid(1153721)]'
hide p1
$ update_portrait('sc031_01 5', 'p39', [l(-14), dark, flip], 5)
$ update_portrait('sc030_01 4', 'p38', [r(-12), light], 6)
play sfx2 "other_7043.ogg"
c383 '[convertstrid(1153722)]'
stop music
hide p39
$ update_portrait('sc030_01 4', 'p38', [r(-12), dark], 5)
$ update_portrait('sc032_01 2', 'p40', [l(-17), light, flip], 6)
c401 '[convertstrid(1153723)]' with shake
$ play_music("ed7151.ogg")
$ update_portrait('sc032_01 2', 'p40', [l(-17), dark, flip], 5)
$ update_portrait('sc030_01 4', 'p38', [r(-12), light], 6)
c383 '[convertstrid(1153724)]'
hide p38
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[convertstrid(1153725)]'
hide p40
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('sc031_01 2', 'p39', [l(-14), light, flip], 6)
c391 '[convertstrid(1153726)]'
$ update_portrait('sc031_01 2', 'p39', [l(-14), dark, flip], 5)
$ update_portrait('oc002_01 16', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1153727)]'
hide p39
$ update_portrait('oc002_01 16', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 11', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1153728)]'
hide p2
$ update_portrait('oc004_01 11', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1153729)]'
hide p4
$ update_portrait('oc001_01 16', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1153730)]'
stop music
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1153731)]'
$ play_music("ed7511.ogg")
$ update_portrait('oc001_01 9', 'p1', [r(-2), r_shake, light], 6)
c13 '[convertstrid(1153732)]'
hide p1
$ update_portrait('sc030_01 4', 'p38', [r(-12), light], 6)
play sfx2 "other_7079.ogg"
c383 '[convertstrid(1153733)]' with shake
hide p3
$ update_portrait('sc030_01 4', 'p38', [r(-12), dark], 5)
$ update_portrait('sc031_01 2', 'p39', [l(-14), light, flip], 6)
c391 '[convertstrid(1153734)]'
$ update_portrait('sc031_01 2', 'p39', [l(-14), dark, flip], 5)
$ update_portrait('sc030_01 4', 'p38', [r(-12), light], 6)
c383 '[convertstrid(1153735)]'
hide p39
$ update_portrait('sc030_01 4', 'p38', [r(-12), dark], 5)
$ update_portrait('sc032_01 5', 'p40', [l(-17), light, flip], 6)
c401 '[convertstrid(1153736)]'
hide p38
$ update_portrait('sc032_01 5', 'p40', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 6)
c23 '[convertstrid(1153737)]'
return