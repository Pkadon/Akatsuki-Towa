label avg10001:

$ play_music("ED6516.ogg")
scene avg_bg_070
show memoryoverlay zorder 2
$ update_narrator('c5001')
window show
with fade_in
play sfx2 "other_7085.ogg"
play sfxvoice "avg_vocal_roi01.ogg"
c5001 '[convertstrid(1002967)]' (what_size=(gui.text_size*1.5)) with shake
scene avg_bg_004
show memoryoverlay zorder 2
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
play sfxvoice "bcv_oc001_hurt_01.ogg"
c13 '[convertstrid(1000001)]'
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1000002)]'
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1000003)]'
$ update_portrait('oc001_01 14', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na08.ogg"
c13 '[convertstrid(1000004)]'
$ update_portrait('oc001_01 3', 'p1', [r(-2), r_shake, light], 6)
c13 '[convertstrid(1000005)]'
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1000006)]'
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1000007)]'
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1000008)]'
$ update_portrait('oc001_01 15', 'p1', [r(-2), r_shake, light], 6)
c13 '[convertstrid(1000009)]'
$ update_portrait('oc001_01 14', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na07.ogg"
c13 '[convertstrid(1000010)]' with shake
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1000011)]'
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1000012)]'
$ play_music("ed7511.ogg")
$ update_portrait('oc001_01 13', 'p1', [r(-2), dark], 5)
play sfx2 "other_7079.ogg"
c5291 '[convertstrid(1100035)]'
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc001_hurt_02.ogg"
c13 '[convertstrid(1100036)]'
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1100037)]'
$ update_portrait('oc001_01 15', 'p1', [r(-2), r_shake, light], 6)
play sfx2 "fight_6029.ogg"
play sfxvoice "avg_vocal_na24.ogg"
c13 '[convertstrid(1100038)]'
$ update_portrait('oc001_01 15', 'p1', [r(-2), dark], 5)
play sfx2 "other_7076.ogg"
c5291 '[convertstrid(1100039)]'
$ update_portrait('oc001_01 9', 'p1', [r_midback(-2), light], 6)
play sfx2 "fight_6024.ogg"
play sfxvoice "avg_vocal_na12.ogg"
c13 '[convertstrid(1100040)]'
return