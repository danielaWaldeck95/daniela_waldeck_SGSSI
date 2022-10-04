encrypted_message = "RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."

# Para conocer la cantidad de ocurrencias de cada caracter y luego sustituir segun probabilidad en el idioma del mensaje encriptado
stored_letters = {}
for char in encrypted_message:
    if char not in stored_letters:
        stored_letters[char] = 1
    else:
        stored_letters[char] += 1

attempt = encrypted_message.replace("X", "\033[31me\033[0m")
attempt = attempt.replace("E", "\033[31ma\033[0m")
attempt = attempt.replace("I", "\033[31mo\033[0m")
attempt = attempt.replace("J", "\033[31mn\033[0m")
attempt = attempt.replace("T", "\033[31ml\033[0m")
attempt = attempt.replace("A", "\033[31md\033[0m")
attempt = attempt.replace("D", "\033[31mp\033[0m")
attempt = attempt.replace("C", "\033[31mi\033[0m")
attempt = attempt.replace("P", "\033[31mm\033[0m")
attempt = attempt.replace("Q", "\033[31mb\033[0m")
attempt = attempt.replace("K", "\033[31mr\033[0m")
attempt = attempt.replace("v", "\033[31mv\033[0m")
attempt = attempt.replace("R", "\033[31mc\033[0m")
attempt = attempt.replace("Z", "\033[31mu\033[0m")
attempt = attempt.replace("N", "\033[31ms\033[0m")
attempt = attempt.replace("H", "\033[31mt\033[0m")
attempt = attempt.replace("G", "\033[31mj\033[0m")
attempt = attempt.replace("O", "\033[31mf\033[0m")
attempt = attempt.replace("U", "\033[31mg\033[0m")
attempt = attempt.replace("F", "\033[31mx\033[0m")
attempt = attempt.replace("M", "\033[31mh\033[0m")
attempt = attempt.replace("S", "\033[31mq\033[0m")
attempt = attempt.replace("V", "\033[31my\033[0m")
attempt = attempt.replace("L", "\033[31mz\033[0m")
print(attempt)
