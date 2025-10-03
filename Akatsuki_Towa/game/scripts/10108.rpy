label avg10108:

$ play_music("ed7103.ogg")
scene avg_bg_007
$ update_narrator('c31')
window show
with fade_in
$ update_portrait('oc003_01 8', 'p3', [l_entrance(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
c31 '[convertstrid(1005965)]'
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1005966)]'
hide p3
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li07.ogg"
c41 '[convertstrid(1005967)]'
hide p1
$ update_portrait('oc004_01 9', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc006_01 1', 'p6', [r_entrance(-5), light], 6)
play sfx2 "other_7047.ogg"
c63 '[convertstrid(1005968)]'
$ update_portrait('oc006_01 1', 'p6', [r(-5), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1005969)]'
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1005970)]'
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc006_01 1', 'p6', [r_exit(-5), light], 6)
c63 '[convertstrid(1005971)]'
hide p6
$ update_portrait('oc001_01 2', 'p1', [r_entrance(-2), light], 6)
c13 '[convertstrid(1005972)]'
hide p4
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1005973)]'
hide p1
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro09.ogg"
c33 '[convertstrid(1005974)]'
hide p3
$ update_portrait('oc006_01 1', 'p6', [r_entrance(-5), light], 6)
play sfx2 "other_7047.ogg"
c63 '[convertstrid(1005975)]'
hide p2
$ update_portrait('oc006_01 1', 'p6', [r(-5), dark], 5)
$ update_portrait('st043_01 2', 'p242', [l_entrance(-17), light, flip], 6)
c2421 '[convertstrid(1005976)]'
hide p6
$ update_portrait('st043_01 2', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('st042_01 1', 'p241', [r_entrance(-14), light], 6)
c2413 '[convertstrid(1005977)]'
$ update_portrait('st042_01 1', 'p241', [r(-14), dark], 5)
$ update_portrait('st043_01 2', 'p242', [l(-17), light, flip], 6)
c2421 '[convertstrid(1005978)]'
$ update_portrait('st043_01 2', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('st042_01 1', 'p241', [r(-14), light], 6)
c2413 '[convertstrid(1005979)]'
$ update_portrait('st042_01 1', 'p241', [r(-14), dark], 5)
$ update_portrait('st043_01 5', 'p242', [l(-17), light, flip], 6)
c2421 '[convertstrid(1005980)]'
$ update_portrait('st043_01 1', 'p242', [l(-17), light, flip], 6)
c2421 '[convertstrid(1005981)]'
$ update_portrait('st043_01 1', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('st042_01 5', 'p241', [r(-14), light], 6)
c2413 '[convertstrid(1005982)]'
$ update_portrait('st042_01 5', 'p241', [r(-14), dark], 5)
$ update_portrait('st043_01 2', 'p242', [l(-17), light, flip], 6)
c2421 '[convertstrid(1005983)]'
$ update_portrait('st043_01 2', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('st042_01 2', 'p241', [r(-14), light], 6)
c2413 '[convertstrid(1005984)]'
$ update_portrait('st042_01 2', 'p241', [r(-14), dark], 5)
$ update_portrait('st043_01 5', 'p242', [l(-17), light, flip], 6)
c2421 '[convertstrid(1001686)]'
$ update_portrait('st043_01 5', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('st042_01 5', 'p241', [r(-14), light], 6)
c2413 '[convertstrid(1005986)]'
$ update_portrait('st042_01 5', 'p241', [r(-14), dark], 5)
$ update_portrait('st043_01 2', 'p242', [l(-17), l_shake, light, flip], 6)
c2421 '[convertstrid(1005987)]'
$ update_portrait('st043_01 2', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('st042_01 2', 'p241', [r(-14), r_shake, light], 6)
c2413 '[convertstrid(1005987)]'
hide p241
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro10.ogg"
c33 '[convertstrid(1005988)]'
hide p242
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1005989)]'
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1005990)]'
hide p3
$ update_portrait('st043_01 4', 'p242', [r(-17), light], 6)
c2423 '[convertstrid(1005991)]'
hide p1
$ update_portrait('st043_01 4', 'p242', [r(-17), dark], 5)
$ update_portrait('st042_01 2', 'p241', [l(-14), light, flip], 6)
c2411 '[convertstrid(1005992)]'
hide p242
$ update_portrait('st042_01 2', 'p241', [l(-14), dark, flip], 5)
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 6)
play sfx2 "other_7091.ogg"
play sfxvoice "avg_vocal_li18.ogg"
c43 '[convertstrid(1005993)]'
hide p241
$ update_portrait('oc004_01 8', 'p4', [r(-5), dark], 5)
$ update_portrait('oc006_01 1', 'p6', [l_midback(-5), light, flip], 6)
c61 '[convertstrid(1005994)]'
hide p4
$ update_portrait('oc006_01 1', 'p6', [l(-5), dark, flip], 5)
$ update_portrait('st043_01 2', 'p242', [r(-17), light], 6)
play sfx2 "other_7057.ogg"
c2423 '[convertstrid(1005995)]'
hide p6
$ update_portrait('st043_01 2', 'p242', [r(-17), dark], 5)
$ update_portrait('st042_01 2', 'p241', [l(-14), light, flip], 6)
c2411 '[convertstrid(1005996)]'
hide p242
$ update_portrait('st042_01 2', 'p241', [l(-14), dark, flip], 5)
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li07.ogg"
c43 '[convertstrid(1005997)]'
hide p241
$ update_portrait('oc004_01 9', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1005998)]'
hide p4
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1005999)]'
$ update_portrait('oc003_01 8', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch11.ogg"
c21 '[convertstrid(1006000)]'
hide p2
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1006001)]'
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 12', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1006002)]'
hide p1
$ update_portrait('oc003_01 12', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1006003)]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1006004)]'
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1006005)]'
hide p3
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
c13 '[convertstrid(1006006)]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('st043_01 2', 'p242', [l(-17), light, flip], 6)
c2421 '[convertstrid(1006007)]'
$ update_portrait('st043_01 4', 'p242', [l(-17), light, flip], 6)
c2421 '[convertstrid(1006008)]'
$ update_portrait('st043_01 4', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1006009)]'
hide p242
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro14.ogg"
c31 '[convertstrid(1006010)]'
hide p1
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('st042_01 2', 'p241', [r(-14), light], 6)
c2413 '[convertstrid(1006011)]'
$ update_portrait('st042_01 4', 'p241', [r(-14), light], 6)
c2413 '[convertstrid(1006012)]'
hide p3
$ update_portrait('st042_01 4', 'p241', [r(-14), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1006013)]'
hide p241
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[convertstrid(1006014)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1006015)]'
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1006016)]'
hide p1
$ update_portrait('oc004_01 9', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1006017)]'
hide p4
$ update_portrait('oc003_01 8', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch12.ogg"
c21 '[convertstrid(1006018)]'
hide p3
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1006019)]'
hide p2
$ update_portrait('oc004_01 2', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1006020)]'
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li18.ogg"
c43 '[convertstrid(1006021)]'
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1006022)]'
$ update_portrait('oc004_01 23', 'p4', [r(-5), r_shake, light], 6)
c43 '[convertstrid(1006023)]'
hide p1
$ update_portrait('oc004_01 23', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1006024)]'
hide p4
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
c13 '[convertstrid(1006025)]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('st043_01 2', 'p242', [l(-17), light, flip], 6)
c2421 '[convertstrid(1006026)]'
hide p1
$ update_portrait('st043_01 2', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('st042_01 4', 'p241', [r(-14), light], 6)
c2413 '[convertstrid(1006027)]'
hide p242
$ update_portrait('st042_01 4', 'p241', [r(-14), dark], 5)
$ update_portrait('oc001_01 9', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1006028)]'
hide p241
$ update_portrait('oc001_01 9', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('uc002_03 2', 'p543', [r(-23), light], 6)
c5433 '[convertstrid(1006029)]'
hide p1
$ update_portrait('uc002_03 2', 'p543', [r(-23), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1006030)]'
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('uc002_03 2', 'p543', [r_exit(-23), light], 6)
c5433 '[convertstrid(1006031)]'
hide p543
hide p4
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
c31 '[convertstrid(1006032)]'
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1006033)]'
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1006034)]'
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('st043_01 2', 'p242', [r(-17), r_shake, light], 6)
c2423 '[convertstrid(1006035)]'
hide p3
$ update_portrait('st043_01 2', 'p242', [r(-17), dark], 5)
$ update_portrait('st042_01 2', 'p241', [l(-14), light, flip], 6)
c2411 '[convertstrid(1006036)]'
hide p241
hide p242
c0 '[convertstrid(1006037)]'
$ update_portrait('st043_01 2', 'p242', [r(-17), light], 6)
c2423 '[convertstrid(1006038)]'
$ update_portrait('st043_01 2', 'p242', [r(-17), dark], 5)
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1006039)]'
hide p3
$ update_portrait('st043_01 5', 'p242', [l(-17), light, flip], 6)
c2421 '[convertstrid(1006040)]'
$ update_portrait('st043_01 5', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('st042_01 1', 'p241', [r(-14), light], 6)
c2413 '[convertstrid(1006041)]'
$ update_portrait('st042_01 1', 'p241', [r(-14), dark], 5)
$ update_portrait('st043_01 2', 'p242', [l(-17), light, flip], 6)
c2421 '[convertstrid(1006042)]'
hide p241
$ update_portrait('st043_01 2', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro10.ogg"
c33 '[convertstrid(1006043)]'
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
$ update_portrait('st043_01 5', 'p242', [l(-17), light, flip], 6)
c2421 '[convertstrid(1006044)]'
hide p3
$ update_portrait('st043_01 5', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('st042_01 5', 'p241', [r(-14), light], 6)
c2413 '[convertstrid(1006045)]'
hide p242
$ update_portrait('st042_01 5', 'p241', [r(-14), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
play sfx2 "other_7091.ogg"
c41 '[convertstrid(1005993)]'
hide p241
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc006_01 1', 'p6', [r(-5), light], 6)
c63 '[convertstrid(1005994)]'
hide p4
$ update_portrait('oc006_01 1', 'p6', [r(-5), dark], 5)
$ update_portrait('st043_01 2', 'p242', [l(-17), light, flip], 6)
c2421 '[convertstrid(1006048)]'
hide p6
$ update_portrait('st043_01 2', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('st042_01 2', 'p241', [r(-14), light], 6)
c2413 '[convertstrid(1006049)]'
$ update_portrait('st042_01 2', 'p241', [r(-14), dark], 5)
$ update_portrait('st043_01 2', 'p242', [l(-17), light, flip], 6)
c2421 '[convertstrid(1006050)]'
hide p241
$ update_portrait('st043_01 2', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na22.ogg"
c13 '[convertstrid(1006051)]'
hide p242
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1006052)]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1006053)]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1006054)]'
hide p2
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('st043_01 2', 'p242', [l(-17), light, flip], 6)
c2421 '[convertstrid(1006055)]'
hide p3
$ update_portrait('st043_01 2', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1006056)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('st043_01 1', 'p242', [l(-17), light, flip], 6)
c2421 '[convertstrid(1006057)]'
$ update_portrait('st043_01 1', 'p242', [l(-17), light, flip], 6)
c2421 '[convertstrid(1006058)]'
hide p1
$ update_portrait('st043_01 1', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('st042_01 2', 'p241', [r(-14), light], 6)
c2413 '[convertstrid(1006059)]'
hide p241
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro19.ogg"
c33 '[convertstrid(1006060)]'
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('st043_01 1', 'p242', [l(-17), light, flip], 6)
c2421 '[convertstrid(1006061)]'
hide p3
$ update_portrait('st043_01 1', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
play sfxvoice "bcv_oc002_die_01.ogg"
c23 '[convertstrid(1005841)]'
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('st043_01 5', 'p242', [l(-17), light, flip], 6)
c2421 '[convertstrid(1006063)]'
hide p2
$ update_portrait('st043_01 5', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('st042_01 1', 'p241', [r(-14), light], 6)
c2413 '[convertstrid(1006064)]'
hide p242
$ update_portrait('st042_01 1', 'p241', [r(-14), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1006065)]'
hide p4
$ update_portrait('st043_01 2', 'p242', [l(-17), light, flip], 6)
c2421 '[convertstrid(1006066)]'
$ update_portrait('st043_01 2', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('st042_01 2', 'p241', [r(-14), light], 6)
c2413 '[convertstrid(1006067)]'
$ update_portrait('st042_01 5', 'p241', [r(-14), light], 6)
c2413 '[convertstrid(1001686)]'
hide p241
$ update_portrait('st043_01 5', 'p242', [r(-17), light], 6)
c2423 '[convertstrid(1001686)]'
$ update_portrait('st043_01 5', 'p242', [r(-17), dark], 5)
$ update_portrait('oc004_01 14', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1006069)]'
hide p242
$ update_portrait('oc004_01 14', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('st042_01 4', 'p241', [r(-14), light], 6)
c2413 '[convertstrid(1006070)]'
hide p241
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1006071)]'
hide p4
$ update_portrait('oc003_01 8', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1006072)]'
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 7', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1006073)]'
hide p1
$ update_portrait('oc003_01 7', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1006074)]'
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1006075)]'
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1006076)]'
hide p2
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na10.ogg"
c11 '[convertstrid(1006077)]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro19.ogg"
c33 '[convertstrid(1006078)]'
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1006079)]'
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1006080)]'
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1006081)]'
hide p1
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li06.ogg"
c41 '[convertstrid(1006082)]'
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1006083)]'
hide p3
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1006084)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1006085)]'
hide p1
$ update_portrait('oc004_01 9', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1006086)]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 6', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li30.ogg"
c41 '[convertstrid(1006087)]'
hide p2
$ update_portrait('oc004_01 6', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1006088)]'
hide p4
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1006089)]'
return