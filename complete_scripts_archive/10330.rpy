label avg10330:

$ play_music("ed7110.ogg")
scene avg_bg_030
$ update_narrator('c21')
window show
with fade_in
$ update_portrait('oc002_01 8', 'p2', [l_entrance(-3), light, flip], 6)
play sfx2 "other_7047.ogg"
c21 '[convertstrid(1130875)]'
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1130876)]'
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('sc060_01 5', 'p65', [r_entrance(-16), light], 6)
play sfx2 "other_7020.ogg"
c653 '[convertstrid(1130877)]'
hide p65
$ update_portrait('sc045_01 2', 'p52', [r(-11), light], 6)
c523 '[convertstrid(1130878)]'
hide p52
$ update_portrait('sc038_01 2', 'p45', [r(-1), light], 6)
c453 '[convertstrid(1130882)]'
hide p2
$ update_portrait('sc038_01 2', 'p45', [r(-1), dark], 5)
$ update_portrait('oc004_01 23', 'p4', [l(-5), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_li13.ogg"
c41 '[convertstrid(1130883)]'
hide p45
$ update_portrait('oc004_01 23', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('sc039_01 2', 'p46', [r(-13), light], 6)
c463 '[convertstrid(1130884)]'
$ update_portrait('sc039_01 2', 'p46', [r(-13), dark], 5)
$ update_portrait('oc004_01 24', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li08.ogg"
c41 '[convertstrid(1130885)]'
hide p46
$ update_portrait('oc004_01 24', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro03.ogg"
c33 '[convertstrid(1130886)]'
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l_midback(-5), light, flip], 6)
c41 '[convertstrid(1130887)]'
stop music
scene avg_bg_070
$ update_narrator('c0')
with fade
c0 '[convertstrid(1130888)]'
c0 '[convertstrid(1130889)]'
c0 '[convertstrid(1130890)]'
$ play_music("ed7151.ogg")
scene avg_bg_030
$ update_portrait('oc002_01 19', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
with fade
play sfxvoice "avg_vocal_ch25.ogg"
c21 '[convertstrid(1130891)]'
$ update_portrait('oc002_01 4', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[convertstrid(1130892)]'
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1130893)]'
hide p2
$ update_portrait('oc004_01 9', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1130894)]'
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1130895)]'
hide p4
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1130896)]'
hide p3
$ update_portrait('sc038_01 4', 'p45', [r(-1), light], 6)
c453 '[convertstrid(1130897)]'
$ update_portrait('sc038_01 4', 'p45', [r(-1), dark], 5)
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1130898)]'
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc038_01 4', 'p45', [r(-1), light], 6)
c453 '[convertstrid(1130899)]'
$ update_portrait('sc038_01 3', 'p45', [r(-1), light], 6)
c453 '[convertstrid(1130900)]'
$ update_portrait('sc038_01 4', 'p45', [r(-1), light], 6)
c453 '[convertstrid(1130901)]'
hide p1
$ update_portrait('sc038_01 4', 'p45', [r(-1), dark], 5)
$ update_portrait('oc004_01 21', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1130902)]'
hide p45
$ update_portrait('oc004_01 21', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('sc041_01 4', 'p48', [r(-9), light], 6)
c483 '[convertstrid(1130903)]'
hide p4
$ update_portrait('sc041_01 4', 'p48', [r(-9), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1130904)]'
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1130905)]'
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc041_01 3', 'p48', [r(-9), light], 6)
c483 '[convertstrid(1130906)]'
$ update_portrait('sc041_01 3', 'p48', [r(-9), dark], 5)
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
play sfx2 "other_7007.ogg"
play sfxvoice "bcv_oc001_hurt_01.ogg"
c11 '[convertstrid(1130907)]' with shake
hide p1
$ update_portrait('oc002_01 7', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch31.ogg"
c21 '[convertstrid(1130908)]'
hide p2
$ update_portrait('oc001_01 9', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1130909)]'
$ update_portrait('oc001_01 9', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc041_01 2', 'p48', [r(-9), light], 6)
c483 '[convertstrid(1130910)]'
hide p1
$ update_portrait('sc041_01 2', 'p48', [r(-9), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1130911)]'
hide p2
$ update_portrait('oc001_01 9', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1130912)]'
$ update_portrait('oc001_01 9', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc041_01 4', 'p48', [r(-9), light], 6)
c483 '[convertstrid(1130913)]'
hide p48
$ update_portrait('sc040_01 4', 'p47', [r(-9), light], 6)
c473 '[convertstrid(1130914)]'
$ update_portrait('sc040_01 4', 'p47', [r(-9), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1130915)]'
hide p1
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1130916)]'
hide p47
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('sc045_01 3', 'p52', [r(-11), light], 6)
c523 '[convertstrid(1130917)]'
$ update_portrait('sc045_01 1', 'p52', [r(-11), light], 6)
c523 '[convertstrid(1130918)]'
hide p52
$ update_portrait('sc041_01 5', 'p48', [r(-9), light], 6)
c483 '[convertstrid(1130919)]'
$ update_portrait('sc041_01 1', 'p48', [r(-9), light], 6)
c483 '[convertstrid(1130920)]'
$ update_portrait('sc041_01 1', 'p48', [r(-9), dark], 5)
$ update_portrait('oc004_01 17', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li18.ogg"
c41 '[convertstrid(1130924)]'
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1130925)]'
$ update_portrait('oc004_01 14', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1130926)]'
hide p48
$ update_portrait('oc004_01 14', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1130927)]'
$ update_portrait('oc003_01 7', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1130928)]'
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1130929)]'
hide p4
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1130930)]'
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1130931)]'
hide p3
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc038_01 7', 'p45', [r(-1), light], 6)
c453 '[convertstrid(1130932)]'
$ update_portrait('sc038_01 4', 'p45', [r(-1), light], 6)
c453 '[convertstrid(1130933)]'
hide p1
$ update_portrait('sc038_01 4', 'p45', [r(-1), dark], 5)
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1130934)]'
hide p45
$ update_portrait('oc003_01 7', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('sc039_01 4', 'p46', [r(-13), light], 6)
c463 '[convertstrid(1130935)]'
$ update_portrait('sc039_01 4', 'p46', [r(-13), light], 6)
c463 '[convertstrid(1130936)]'
hide p46
$ update_portrait('sc038_01 2', 'p45', [r(-1), light], 6)
c453 '[convertstrid(1130937)]'
hide p3
hide p45
c0 '[convertstrid(1130938)]'
c0 '[convertstrid(1130939)]'
$ update_portrait('sc038_01 4', 'p45', [r(-1), light], 6)
c453 '[convertstrid(1130940)]'
$ update_portrait('sc038_01 4', 'p45', [r(-1), light], 6)
c453 '[convertstrid(1130941)]'
$ update_portrait('sc038_01 3', 'p45', [r(-1), light], 6)
c453 '[convertstrid(1130942)]'
$ update_portrait('sc038_01 4', 'p45', [r(-1), light], 6)
c453 '[convertstrid(1130943)]'
$ update_portrait('sc038_01 4', 'p45', [r(-1), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1130944)]'
hide p45
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('sc041_01 5', 'p48', [r(-9), light], 6)
c483 '[convertstrid(1130945)]'
hide p2
$ update_portrait('sc041_01 5', 'p48', [r(-9), dark], 5)
$ update_portrait('sc039_01 4', 'p46', [l(-13), light, flip], 6)
c461 '[convertstrid(1130946)]'
$ update_portrait('sc039_01 5', 'p46', [l(-13), light, flip], 6)
c461 '[convertstrid(1130947)]'
hide p48
$ update_portrait('sc039_01 5', 'p46', [l(-13), dark, flip], 5)
$ update_portrait('sc038_01 2', 'p45', [r(-1), light], 6)
c453 '[convertstrid(1130948)]'
hide p46
$ update_portrait('sc038_01 2', 'p45', [r(-1), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1130949)]'
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1130950)]'
hide p45
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('sc060_01 5', 'p65', [r(-16), light], 6)
c653 '[convertstrid(1130951)]'
hide p2
$ update_portrait('sc060_01 5', 'p65', [r(-16), dark], 5)
$ update_portrait('oc004_01 11', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1130952)]'
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1130953)]'
hide p65
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1130954)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1130955)]'
hide p1
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('sc040_01 2', 'p47', [r(-9), light], 6)
c473 '[convertstrid(1130956)]'
hide p4
$ update_portrait('sc040_01 2', 'p47', [r(-9), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1130957)]'
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1130958)]'
hide p47
$ update_portrait('oc003_01 7', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('sc038_01 2', 'p45', [r(-1), light], 6)
c453 '[convertstrid(1130959)]'
hide p3
$ update_portrait('sc038_01 2', 'p45', [r(-1), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1130960)]'
$ update_portrait('oc004_01 14', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1130961)]'
$ update_portrait('oc004_01 11', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1130962)]'
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1130963)]'
$ update_portrait('oc004_01 14', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1130964)]'
$ update_portrait('oc004_01 3', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1130965)]'
$ update_portrait('oc004_01 16', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1130996)]'
hide p45
$ update_portrait('oc004_01 16', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('sc040_01 3', 'p47', [r(-9), r_shake, light], 6)
c473 '[convertstrid(1130967)]'
hide p4
$ update_portrait('sc040_01 3', 'p47', [r(-9), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1130968)]'
hide p47
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('sc038_01 4', 'p45', [r(-1), light], 6)
c453 '[convertstrid(1130969)]'
hide p3
$ update_portrait('sc038_01 4', 'p45', [r(-1), dark], 5)
$ update_portrait('oc004_01 17', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1130970)]'
$ update_portrait('oc004_01 21', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1130971)]'
hide p4
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1130972)]'
hide p45
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1130973)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1130974)]'
hide p1
$ update_portrait('sc038_01 4', 'p45', [r(-1), light], 6)
c453 '[convertstrid(1130975)]'
hide p2
$ update_portrait('sc038_01 4', 'p45', [r(-1), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1130976)]'
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('sc038_01 1', 'p45', [r(-1), light], 6)
c453 '[convertstrid(1130977)]'
$ update_portrait('sc038_01 4', 'p45', [r(-1), light], 6)
c453 '[convertstrid(1130978)]'
$ update_portrait('sc038_01 4', 'p45', [r(-1), dark], 5)
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro10.ogg"
c31 '[convertstrid(1130979)]'
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('sc038_01 4', 'p45', [r(-1), light], 6)
c453 '[convertstrid(1130980)]'
$ update_portrait('sc038_01 4', 'p45', [r(-1), dark], 5)
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1130981)]'
hide p3
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1130982)]'
hide p45
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc060_01 5', 'p65', [r(-16), light], 6)
c653 '[convertstrid(1130983)]'
$ update_portrait('sc060_01 1', 'p65', [r(-16), light], 6)
c653 '[convertstrid(1130984)]'
$ update_portrait('sc060_01 1', 'p65', [r(-16), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1130985)]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1130986)]'
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1130987)]'
hide p65
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1130988)]'
hide p2
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1130989)]'
hide p4
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('sc039_01 1', 'p46', [r(-13), light], 6)
c463 '[convertstrid(1130990)]'
hide p46
$ update_portrait('sc040_01 1', 'p47', [r(-9), light], 6)
c473 '[convertstrid(1130991)]'
$ update_portrait('sc040_01 4', 'p47', [r(-9), light], 6)
c473 '[convertstrid(1130992)]'
$ update_portrait('sc040_01 4', 'p47', [r(-9), dark], 5)
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1130993)]'
$ update_portrait('oc003_01 18', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1130994)]'
hide p3
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1130995)]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1130966)]'
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1130997)]'
hide p47
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc038_01 5', 'p45', [r(-1), light], 6)
c453 '[convertstrid(1130998)]'
return