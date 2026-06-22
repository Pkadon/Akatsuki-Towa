label avg1188:

$ play_music("ED6107.ogg")
scene avg_bg_029
$ update_narrator('c13')
window show
with fade_in
$ update_portrait('oc001_01 4', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(2106934)]' (**arg(1, 2106934))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2106935)]' (**arg(2, 2106935))
hide p1
$ update_narrator('c25991')
with fade
get_char('c25991') '[convertstrid(2106936)]' (**arg(3, 2106936))
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2106937)]' (**arg(4, 2106937))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc009_01 5', 'p17', [l(-13), light, flip], 6)
get_char('c171') '[convertstrid(2106938)]' (**arg(5, 2106938))
$ update_portrait('sc009_01 1', 'p17', [l(-13), light, flip], 6)
get_char('c171') '[convertstrid(2106939)]' (**arg(6, 2106939))
$ update_portrait('sc009_01 1', 'p17', [l(-13), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2106940)]' (**arg(7, 2106940))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc009_01 1', 'p17', [l(-13), light, flip], 6)
get_char('c171') '[convertstrid(2106941)]' (**arg(8, 2106941))
$ update_portrait('sc009_01 1', 'p17', [l(-13), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2106942)]' (**arg(9, 2106942))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2106943)]' (**arg(10, 2106943))
stop music
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc009_01 4', 'p17', [l(-13), light, flip], 6)
play sfx2 "fight_6027.ogg"
get_char('c171') '[convertstrid(2106944)]' (**arg(11, 2106944)) with shake
$ play_music("ed7511.ogg")
$ update_portrait('sc009_01 4', 'p17', [l(-13), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2106945)]' (**arg(12, 2106945))
hide p17
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('uc004_02 2', 'p570', [l(-9), light, flip], 6)
get_char('c5701') '[convertstrid(2106946)]' (**arg(13, 2106946))
hide p570
play sfx2 "fight_6021.ogg"
get_char('c26001') '[convertstrid(2106947)]' (**arg(14, 2106947)) with shake
$ update_portrait('uc004_02 3', 'p570', [l(-9), light, flip], 6)
play sfx2 "fight_6019.ogg"
get_char('c5701') '[convertstrid(2106948)]' (**arg(15, 2106948))
$ update_portrait('uc004_02 3', 'p570', [l(-9), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfx2 "fight_6011.ogg"
get_char('c13') '[convertstrid(2106949)]' (**arg(16, 2106949))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('uc004_02 3', 'p570', [l(-9), light, flip], 6)
play sfx2 "fight_6012.ogg"
get_char('c5701') '[convertstrid(2106950)]' (**arg(17, 2106950))
hide p570
$ update_portrait('sc009_01 4', 'p17', [l(-13), light, flip], 6)
play sfx2 "fight_6005.ogg"
get_char('c171') '[convertstrid(2106951)]' (**arg(18, 2106951))
$ update_portrait('sc009_01 4', 'p17', [l(-13), dark, flip], 5)
$ update_portrait('oc001_01 20', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(2106952)]' (**arg(19, 2106952))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2106953)]' (**arg(20, 2106953))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc009_01 2', 'p17', [l(-13), light, flip], 6)
get_char('c171') '[convertstrid(2106954)]' (**arg(21, 2106954))
hide p17
$ update_portrait('uc004_02 1', 'p570', [l(-9), light, flip], 6)
get_char('c5701') '[convertstrid(2106955)]' (**arg(22, 2106955))
$ update_portrait('uc004_02 1', 'p570', [l(-9), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2106956)]' (**arg(23, 2106956)) with shake
hide p570
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('sc009_01 4', 'p17', [l(-13), light, flip], 6)
get_char('c171') '[convertstrid(2106957)]' (**arg(24, 2106957))
hide p17
$ update_portrait('uc004_02 3', 'p570', [l(-9), light, flip], 6)
get_char('c5701') '[convertstrid(2106958)]' (**arg(25, 2106958))
hide p570
play sfx2 "other_7045.ogg"
get_char('c26001') '[convertstrid(2106959)]' (**arg(26, 2106959)) with shake
$ update_portrait('oc001_01 19', 'p1', [r_midback(-2), light], 6)
get_char('c13') '[convertstrid(2106960)]' (**arg(27, 2106960))
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('sc009_01 2', 'p17', [l(-13), light, flip], 6)
get_char('c171') '[convertstrid(2106961)]' (**arg(28, 2106961))
hide p17
hide p1
$ update_narrator('c26003')
with fade
get_char('c26003') '[convertstrid(2106962)]' (**arg(29, 2106962))
get_char('c26003') '[convertstrid(2106963)]' (**arg(30, 2106963))
$ update_portrait('oc001_01 9', 'p1', [r_midback(-2), light], 6)
play sfx2 "fight_6023.ogg"
get_char('c13') '[convertstrid(2106964)]' (**arg(31, 2106964))
hide p1
get_char('c26003') '[convertstrid(2106965)]' (**arg(32, 2106965))
get_char('c26003') '[convertstrid(2106966)]' (**arg(33, 2106966))
$ play_music("ed7151.ogg")
scene avg_bg_036
$ update_narrator('c13')
with fade
$ update_portrait('oc001_01 19', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(2106967)]' (**arg(34, 2106967))
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2106968)]' (**arg(35, 2106968))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2106969)]' (**arg(36, 2106969))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc009_01 3', 'p17', [l(-13), light, flip], 6)
get_char('c171') '[convertstrid(2106970)]' (**arg(37, 2106970))
$ update_portrait('sc009_01 3', 'p17', [l(-13), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2106971)]' (**arg(38, 2106971))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc009_01 2', 'p17', [l(-13), light, flip], 6)
get_char('c171') '[convertstrid(2106972)]' (**arg(39, 2106972))
hide p1
$ update_portrait('sc009_01 2', 'p17', [l(-13), dark, flip], 5)
$ update_portrait('st013_01 4', 'p212', [r(-16), light], 6)
get_char('c2123') '[convertstrid(2106973)]' (**arg(40, 2106973))
$ update_portrait('st013_01 4', 'p212', [r(-16), light], 6)
get_char('c2123') '[convertstrid(2106974)]' (**arg(41, 2106974))
$ update_portrait('st013_01 4', 'p212', [r(-16), dark], 5)
$ update_portrait('sc009_01 4', 'p17', [l(-13), light, flip], 6)
get_char('c171') '[convertstrid(2106975)]' (**arg(42, 2106975))
hide p212
$ update_portrait('sc009_01 4', 'p17', [l(-13), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2106976)]' (**arg(43, 2106976))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc009_01 1', 'p17', [l(-13), light, flip], 6)
get_char('c171') '[convertstrid(2106977)]' (**arg(44, 2106977))
$ update_portrait('sc009_01 1', 'p17', [l(-13), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(2106978)]' (**arg(45, 2106978))
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2106979)]' (**arg(46, 2106979))
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('sc009_01 4', 'p17', [l(-13), light, flip], 6)
get_char('c171') '[convertstrid(2106980)]' (**arg(47, 2106980))
hide p1
$ update_portrait('sc009_01 4', 'p17', [l(-13), dark, flip], 5)
$ update_portrait('st013_01 4', 'p212', [r(-16), light], 6)
get_char('c2123') '[convertstrid(2106981)]' (**arg(48, 2106981))
$ update_portrait('st013_01 4', 'p212', [r(-16), dark], 5)
$ update_portrait('sc009_01 4', 'p17', [l(-13), light, flip], 6)
get_char('c171') '[convertstrid(2106982)]' (**arg(49, 2106982))
$ update_portrait('sc009_01 4', 'p17', [l(-13), dark, flip], 5)
$ update_portrait('st013_01 4', 'p212', [r(-16), light], 6)
get_char('c2123') '[convertstrid(2106983)]' (**arg(50, 2106983))
$ update_portrait('st013_01 4', 'p212', [r(-16), dark], 5)
$ update_portrait('sc009_01 4', 'p17', [l(-13), light, flip], 6)
get_char('c171') '[convertstrid(2106984)]' (**arg(51, 2106984))
hide p212
$ update_portrait('sc009_01 4', 'p17', [l(-13), dark, flip], 5)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2106985)]' (**arg(52, 2106985))
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('sc009_01 4', 'p17', [l(-13), light, flip], 6)
get_char('c171') '[convertstrid(2106986)]' (**arg(53, 2106986))
$ update_portrait('sc009_01 4', 'p17', [l(-13), dark, flip], 5)
$ update_portrait('oc001_01 14', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2106987)]' (**arg(54, 2106987)) with shake
$ update_portrait('oc001_01 14', 'p1', [r(-2), dark], 5)
$ update_portrait('sc009_01 2', 'p17', [l(-13), l_shake, light, flip], 6)
get_char('c171') '[convertstrid(2106988)]' (**arg(55, 2106988))
$ update_portrait('sc009_01 2', 'p17', [l(-13), dark, flip], 5)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2106989)]' (**arg(56, 2106989))
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2106990)]' (**arg(57, 2106990))
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2106991)]' (**arg(58, 2106991))
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('sc009_01 4', 'p17', [l(-13), light, flip], 6)
get_char('c171') '[convertstrid(2106992)]' (**arg(59, 2106992))
hide p1
$ update_portrait('sc009_01 4', 'p17', [l(-13), dark, flip], 5)
$ update_portrait('st013_01 2', 'p212', [r(-16), light], 6)
get_char('c2123') '[convertstrid(2106993)]' (**arg(60, 2106993))
$ update_portrait('st013_01 2', 'p212', [r(-16), dark], 5)
$ update_portrait('sc009_01 5', 'p17', [l(-13), light, flip], 6)
get_char('c171') '[convertstrid(2106994)]' (**arg(61, 2106994))
hide p212
$ update_portrait('sc009_01 5', 'p17', [l(-13), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2106995)]' (**arg(62, 2106995))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc009_01 1', 'p17', [l(-13), light, flip], 6)
get_char('c171') '[convertstrid(2106996)]' (**arg(63, 2106996))
$ update_portrait('sc009_01 5', 'p17', [l(-13), light, flip], 6)
play sfx2 "fight_6024.ogg"
get_char('c171') '[convertstrid(2106997)]' (**arg(64, 2106997))
hide p1
$ update_portrait('sc009_01 5', 'p17', [l(-13), dark, flip], 5)
$ update_portrait('st013_01 1', 'p212', [r(-16), light], 6)
get_char('c2123') '[convertstrid(2106998)]' (**arg(65, 2106998))
$ update_portrait('st013_01 1', 'p212', [r(-16), dark], 5)
$ update_portrait('sc009_01 1', 'p17', [l(-13), light, flip], 6)
get_char('c171') '[convertstrid(2106999)]' (**arg(66, 2106999))
hide p212
$ update_portrait('sc009_01 1', 'p17', [l(-13), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfx2 "fight_6024.ogg"
get_char('c13') '[convertstrid(2107000)]' (**arg(67, 2107000))
stop music
hide p17
hide p1
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
play sfx2 "other_7057.ogg"
get_char('c13') '[convertstrid(2107001)]' (**arg(68, 2107001))
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('st013_01 4', 'p212', [l(-16), light, flip], 6)
get_char('c2121') '[convertstrid(2107002)]' (**arg(69, 2107002))
$ update_portrait('st013_01 4', 'p212', [l(-16), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2107003)]' (**arg(70, 2107003))
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
play sfx2 "other_7018.ogg"
get_char('c13') '[convertstrid(2107004)]' (**arg(71, 2107004))
hide p1
$ update_portrait('sc017_01 4', 'p25', [r(-7), light], 6)
play sfx2 "other_7018.ogg"
get_char('c253') '[convertstrid(2107005)]' (**arg(72, 2107005))
$ update_portrait('sc017_01 4', 'p25', [r(-7), dark], 5)
$ update_portrait('st013_01 4', 'p212', [l(-16), light, flip], 6)
play sfx2 "other_7018.ogg"
get_char('c2121') '[convertstrid(2107006)]' (**arg(73, 2107006))
hide p25
$ update_portrait('st013_01 4', 'p212', [l(-16), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2107007)]' (**arg(74, 2107007))
$ play_music("ED6523.ogg")
hide p212
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('uc004_02 2', 'p570', [l(-9), light, flip], 6)
get_char('c5701') '[convertstrid(2107008)]' (**arg(75, 2107008)) with shake
hide p570
get_char('c26001') '[convertstrid(2107009)]' (**arg(76, 2107009))
$ update_portrait('uc004_02 1', 'p570', [l(-9), light, flip], 6)
get_char('c5701') '[convertstrid(2107010)]' (**arg(77, 2107010))
$ update_portrait('uc004_02 1', 'p570', [l(-9), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2107011)]' (**arg(78, 2107011))
hide p570
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc009_01 1', 'p17', [l(-13), light, flip], 6)
get_char('c171') '[convertstrid(2107012)]' (**arg(79, 2107012))
$ update_portrait('sc009_01 1', 'p17', [l(-13), dark, flip], 5)
$ update_portrait('oc001_01 24', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(2107013)]' (**arg(80, 2107013))
hide p17
$ update_portrait('oc001_01 24', 'p1', [r(-2), dark], 5)
$ update_portrait('st013_01 1', 'p212', [l(-16), light, flip], 6)
get_char('c2121') '[convertstrid(2107014)]' (**arg(81, 2107014))
hide p1
$ update_portrait('st013_01 1', 'p212', [l(-16), dark, flip], 5)
$ update_portrait('sc017_01 4', 'p25', [r(-7), light], 6)
get_char('c253') '[convertstrid(2107015)]' (**arg(82, 2107015))
$ update_portrait('sc017_01 4', 'p25', [r(-7), dark], 5)
$ update_portrait('st013_01 4', 'p212', [l(-16), light, flip], 6)
get_char('c2121') '[convertstrid(2107016)]' (**arg(83, 2107016))
hide p212
$ update_portrait('sc009_01 5', 'p17', [l(-13), light, flip], 6)
get_char('c171') '[convertstrid(2107017)]' (**arg(84, 2107017))
$ update_portrait('sc009_01 1', 'p17', [l(-13), light, flip], 6)
get_char('c171') '[convertstrid(2107018)]' (**arg(85, 2107018))
hide p25
$ update_portrait('sc009_01 1', 'p17', [l(-13), dark, flip], 5)
$ update_portrait('oc001_01 23', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(2107019)]' (**arg(86, 2107019))
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2107020)]' (**arg(87, 2107020))
$ update_portrait('oc001_01 13', 'p1', [r(-2), dark], 5)
$ update_portrait('sc009_01 5', 'p17', [l(-13), light, flip], 6)
get_char('c171') '[convertstrid(2107021)]' (**arg(88, 2107021))
$ update_portrait('sc009_01 1', 'p17', [l(-13), light, flip], 6)
get_char('c171') '[convertstrid(2107022)]' (**arg(89, 2107022))
$ update_portrait('sc009_01 1', 'p17', [l(-13), light, flip], 6)
get_char('c171') '[convertstrid(2107023)]' (**arg(90, 2107023))
$ update_portrait('sc009_01 1', 'p17', [l(-13), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2107024)]' (**arg(91, 2107024))
return