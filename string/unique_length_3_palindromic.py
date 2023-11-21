from utils import printarResultadoEsperado


class Solution:
    def countPalindromicSubsequence1(self, s: str) -> int:
        palindroms = set({})
        partial = ""
        for letter in s:
            partial += letter
            if s.count(letter) >= 3:
                palindroms.add(f"{letter}{letter}{letter}")
            if len(partial) >= 2 and letter in partial[0: len(partial) - 1]:
                index = partial.find(letter)
                for i in range(index, len(partial)):
                    if partial[i] != letter:
                        palindrom = f"{partial[index]}{partial[i]}{letter}"
                        palindroms.add(palindrom)
        return len(palindroms)

    def countPalindromicSubsequence(self, s: str) -> int:
        palindromes = set({})
        char_info = {}
        for i in range(0, len(s)):
            letter = s[i]
            if letter not in char_info:
                char_info[letter] = {"count": 1, "first": i, "last": i}
            elif letter in char_info:
                char_info[letter]["count"] += 1
                char_info[letter]["last"] = i
        for char, info in char_info.items():
            if info["count"] >= 3:
                palindromes.add(char + char + char)
            if info["count"] >= 2:
                substring = s[info["first"] + 1: info["last"]]
                middle_chars = set(substring)
                for middle_char in middle_chars:
                    palindrome = char + middle_char + char
                    palindromes.add(palindrome)
        return len(palindromes)


if __name__ == '__main__':
    s = Solution()
    text = "aabca"
    resultado = s.countPalindromicSubsequence(text)
    printarResultadoEsperado(resultado, 3)

    printarResultadoEsperado(s.countPalindromicSubsequence("adc"), 0)
    printarResultadoEsperado(s.countPalindromicSubsequence("bbcbaba"), 4)
    printarResultadoEsperado(s.countPalindromicSubsequence("ckafnafqo"), 4)
    printarResultadoEsperado(s.countPalindromicSubsequence("tnapzbjeznakaxowyeqefiwxpoxswedvabnyyuihjenxmpzxyyokldoijgvekjxxvxsvcnrinonkofilfyllcacophzuusnbyhpxoqtnbhezbvwtnejsxcyxsbffqaxfryagvvzzvjvbdgrwkowqfwthrkkhxvmpqkslrfqcxmeiygryknhocdvwyomdzmcfvetugpldpbytefioyiyxjfqkdhbefrlwbgnodzbrknqeyjdcgjovtdfqobqxyqhqltrpizlxdnjdqezzwjaudlsofkvjykktlkjiksffefwrqxotkqfdcqhvuqbfoejnelskrhtoekufkmwdyiyptwrucawbwixfdfvjxpvmshcoxdknqeomzrxzrdltdjjearvypexzyoxzxbdhkdzurzisycpuaxkewehnxmxbghllbttlcodzqtajxjarsiuwukiysomgxxcrincvucbjeuuwaauwqeqwlwucdsftccyaugbcinmfzpehrwbeaefdozssbeizeqppnhlvtnrzgtbbitqvctsatcpxjrrbgvltmmtizepbjmmywzmxldtkadizqkaurepeckdiakhyofmslyezbybimhgyukaieqrlddhsuwjzblkfigwixzuopifdiqzfpgvmmanctqcmpxygluuhdwbgqivmdhizpnvqypdttfuhukvagdaqtcmxdqoptchhsledydwojisoqqkivahoowbsdbbdnygtziktmonqkevvlcxggqobvfbfgdwnitratmrsobpfpaspjxefnxthonefpiigdhapqnkebutwfotvrxvjbqowgnifeimsslktxmpuryccaabahalsycjqztjhqhaddlyzxdqyuwyecslxshaobrfkjalmeaxrywssfgrzervzbowosusthcjvojxsoiqkpjztdrxrkycgdyqlorxixzdiqtwozuvkvwzonogoytrumivjynvfjktcqlvxeauncdbygkvocvaadeubgykjkshkflpmpbmaiaswjocrqjzmabmxmocssxltgzaiuwfkadwuylnmskyqbpsmxhehicevfmauuxubeirvflsxcdtyoljsansqcmhokbgyjkxxwdeorlzjgbuekogddsabucrpawdxwuemmckqouddnwbnzogtvjfgblwuarykpwtdpuxqtephulabcxdqjkmuxhniiynkwrsypromcminqgghhnixxojhvnkglrtxduhrjoiupeswqfuveqmgmhondpgzvzaeyylzphofblzpmkdejubwhoguyrfxoaiqhlfqogovdoifuvfqyctzhmcvfleefcgippkfccsltjpjohwmunimqvpjspsjufikghgpmaygslukijmsxcgfjzmewqpvvzjtcxcsbcylhwhxfingcbruyyeoyxgvfsbcvedmtsdygawtnanbdbedwvohgecgqtbjalurkoknzyjpsttnknmufpjhpkjjifalqdwutqhgaflmmmwmkbyxxhbmkqlpjnmywmjfxezdshafnakulqhbndlmtausobzyjrlsgdxcjkbhyfokvdogxabwgmbmzymclxqzwygoxvirnrvpruugvlhyhzzbpugvovfymdcojtkicemybixlvemaydgwmypkwhpeeijccuaomczvqzaedzjrvjobxibpzpveekzcpqnvhbpgqscprawrsvjnhskugziigdecpdcldburpsldqyopyfmaeebawgemrksidizkixosauykmzdwgpyxskuqsujamvnfirtnnxzpplyulsootbikqumwyxpgiplhqbfxggnbylklyuhvoknyuqhpbzfrhdgzoiofrcqyadtgrrkxfecyioobzwwaguuyzcldtumdrhcujkeysxqztzeinrfztjiktcnvfequtbzfrxmukqfblajzyqkvzwcvpoddmzsiqaviivhwbhzdgjdikbnbihaziswypwjcgixefughvoowvoprhohxtbxkrgbbypcmmjogpouceqowqafseywnzanhuueobfrfnikpxhgwdkqmzkegdeqdrdbzttrdfyoqsvacfdsuwikrrlfqfjwwrmylgleuvtnfchhetmtblhffwvzhmlduqjzoqdgjgcwnikbycxggyywoyxqzayirooafchtgupqryojjqxiwjtnmlorcxgwfkzbrzldtfcgxkzqxxcypcgptygmhetsymzuxcnfoasytoetzorfvgbevfhblqassjttvlrvejeaevkcebklsesswnxpzpilvprflevlipyuvfhumcpudbtnwokqsvbewugbwobocncgovbmvduscdlkqctlrziaaaravaitvpceycuojutpszirunhheodrohntdvhqbjblapaggiijnnkogdhfirjvujbsqbfkwoquaqqyyebgbdkvdonaqgweymynjtnbgebsqheorskegksjsnfiucwvhzkjttwbkfrirhyxacjkhhovnxutjonezizmvbrarbwgxftjvgiskfdccpnsuopfpqffkifwwsyxpntikmnkowxaevzacucdpygjmsghzdskaqfjudbibdnuhofkmvptkesypnblikcyswhnktvquimklubsdduabfznfkwcwaelitcefxjvneomwloxqzvhzdhouzuigwxtnkfqpdcjravnzpbhoyslgukpoykqvwrvqttrtwcndupqodohuxouwyxcvufuuloybqaoeqlkxqefozfpirxqxnroavhaikrzxolauuktodrcooiqyfovcvwtuiiydvukdpuwhxwvetarnpxkzdzkfcfpvvayjbqcqbtbkeqfplkdsfhamlhesldkwrpiocwsvxyzoybuayrgzflcdyjyfxkmymfzxrcejfkvzimozjelxohpsepbwhbvlhblrvknyxtmnxbvqwxpvcfnzeotmtpglvwowweriaftyaupslrzlskygkudujaocveqiezrraizyrkdbqyboiklpbpuglphoaexaiapsrozprnhdwitnqqhlolvxsljexkkftraqhuzbqzmnjdqxnseviomtunraqrujswrwtksilarexetwgenlkdvpegyrtwuvfyoxockgrxetsyeykzeyfsiprcwycsjaqnyyoaimrvffqdrnpycmmbnspgavfhiliicsjxvmvnglwbygwsqcyuajlqydpmbtdmhdvnwjedivvlbiunullhemiitroipzuispedyxzvlidwwbujfqgydwwvuwbaiafqoechwnjpzmmwzflqlyqdajntejfynueovtebfdvahcjacggesmaemncluxmitjqmjwyiqnurlxoskoeldmbrfusyrzyyieooptwyturpqgogeqsgpxfoikmqtwfvhyoggvupselvwleebbgxmnmcmxipoxgdvtcukuwoewgopyxnnojftsjneqkbvtztfhhxqvwocbvefsxwadpuspjahmqtfpfakmfpczdbddfdrslmrbptcckdedslsrytyfqsaolinrlwvucthchurqdiarzdhdvpsjzsvbtrufrpdsmaczdhljijhyfayxuazykjegmbpbszlwafdhqxigwvrqfshgdqxkmxqjxiblrzjlegmcvglcotunbaxuocktcenonvrldaszsmfblgmfcbwjnhhuesaoennjllgadafrwfkvxlglkvcpnvsmazkliiptubprdgarpoybstwqhagzbubpnvhvvykpzqqfprvjohkjcfhbmggeietzrppxzlasxelzramnvoecberauqcyyyugrtopxuldczztnqzynvwzyxhdtlwjnyolnlaevgbmmcvvjcpcqcexrpuplxdskyrwrbbjsguuljbxqehxroijcypwrqeqxyshpjggpalibaocdzjtvkodnoufnnnpwdgmztlolqbhfvptsjtpvzwscfsxizbgocivaexhhddciafhaokbtmxtudgntqoyswmocchnzuvqxqyoqnugzkqlyjixcigircpsrbrmjsjsjbcrbvnuufiksdngjbmbpqhdnpehjjwutolmbugauiljtixouiifuuadwjuwuweksbkipfbsreeehzulwsmktpkcescjznynnkbtzamnkszdwepyluaulzkgevbsxbnftmfipktbozqjgnidotnwjtybrlhjqidfwcyesluptzrqvclutghqtmawojebmsrbwpkgbiqapufsndqfwwawwutnskmhxviegxyglvfnjbpfsoarturgpdlnrwtuolpnexrbzipdmhldjacsptjggxvqpegoczzrmkvyoznnbpyedvafxarklcxnqroumkachjuhxgoyqqcnbmktwqfiwpvuafuavkejvyyplbarlzrkcaqxhccvzfhvocpxpumnautlohdnoqepunoonqdnrqubauljvoxapdydwtjwqpveazoayxjdbliiyllsrdhpucrvohppyledyiplvwxgtgdvjhmviudvdvjvsatbkyxkylfdwmeeoisuacnyversgdkkyyujmbjosycozpvxcvcecwtfvubofabliaygszcnuoihvdompowkdgytktyundmuvcxsbgbjopfemhzuslnwgwdnkhoblfozzxynozifxuqwkdbillhbjqjjkfevpoitcmssrpxcccuyczaihyrbseasjgvysceacdliuowbekvxccfsewzrrgqqahymtsvmoyspjaftbakyqzuarpajywlnstboqxyzipxyjtgjodjbbzopqklxvbosmbsgmgrsyrohpzjfamjweifqvbfjgxecnebeysduiwbtabxkrjatoxngdxckfdyhryyltzozlwwcpplebygrwuxdjncmmapalciesoelycusejxunxsrolunfjocpitrmscobbzignvpfojynpxuhyibcnetebopnqvfreghmhfdtnckyjpfadqaafbysfdsmwdwgsbudcibgfrviugvljxcndbaepkwrtmjpwetndugvtvbkeoufdmnjojvvxltxjsycnkjhhtgrllzrpefkaqjldedwdhdfkdvirsgdrwqynmzyqtydgivcprgfigdzzyzejbnfgfvvgcvwnkjsjmsxogilpxuguxqyjgjmwkypnzbfhcijnxoyyxhcitpiyokvewglzdjszgkyhzyqpgxyvhiisbofufyranrdyvxddjocyhejzhxlxugvqrbmqeqvanuwvfllpkiemcxqbtsvvybyjqrbadwediirydahzrdxtnqczxffqjeuespeswuiszjxrfgequlsenpajmsxvufflnzmcbzbepudnewjcmecqyzfzrqecwrvlsgwumitdfzfrdyxnqthzizwosrrweykjvqzfrxgxumubqnhrmcgmiwyuqiarfkkburfvmjbsubiouyrjlsboxilaycspfiojemadgleaqqcschyotlyknqkonfemmcpudqraysznmojvyyrxsiccuieyruqedbdbvumjzolxmsakokirlkopyxcvkjrawakjsmatzoqzlcqqdsffspsejeekfhzwpxqooikxklhigxythgbxpkyptgswhlfwwgnrrodbikpmyzrnunwhgcaxodrcmbixnfqujmpwdgbhlhydpovdtjdctlwwnpepqvzoluxpygjhgikcfojxheverdwflekraglpnsukvvauzqsxohtyducrmxbgzhvbfuvyevphketsttfdzqgddkzfwffgmbrrllyawdmptixbhjbyegpuveahxubolyuvuxaleeuhwbvsxgwmucxqrigcupwybjonxerqiwbepuprkthgntymqlubedcbnzbszoutbxzbwwmsuypjpqgjptxccexytgoeawdcerrgwjyxtaofzhlxannnpihaewpjnjpwermqxkqfypigexmuejdkxjcvdroydhbyytfditsklmsekvsrybjignqocfcrtbhnwsevcwcvujhrwsnwonzhatciobihdvaueyxmqmvnuyqhwtudldhepsldbehbhpnuctyxowwcwlvkpzhrcescobwkareaaytofkwaqiegngsyoekveutblnlvtyweoxwnxrwfvktnqwzxttelgozczeruffpconzjetsbmstyaymkqkqjpaxncrguqmlklnczkwqohrerzvdkjykjewocifqpxeiprqalhdwagmtkpzblqmoophrgjqokbnuuwcmhlyikpvcjungiuequwievzedlkhpbvengnuawoerbmrogpmvtcjzgdyuxbfrstkpwpqazjhotelovzlonmsadmkqactlxdgxhzdpbmryoyvjhbdudxplmileyepifqrlammkorippicvgfavzhsfevxbtkryybsmyqqmeunogjiroephrjsikzijcbibwbiclhmtqjdlnttculjhuofhxfimnfdfcurgqxzlamnexbummavlibelhirysmuncoclmhwmtljevpbifkpoxqlzipourcnompngysesoknxehhyuhtxrsplowvxisjnytvbdlptpxvvvhoqxlcaiphzyvuufmwnkncsqfntwccgzmohxoxaurwvovvlpjdwypfucvinttmttrfratdgpaynwzhqidsbbnvuwsbiwhsfbisumjkxcrnpofgqsqozzvljylgqwvgmejwchkrbdngmlwoktjaxhnjgbskaczmyqfnvxkgzzarodzadkkyncqrlnppuyoobmgtxwqraenthplhiycsvtnxdmlxazuyzutvvutahfnnbmoltzfgktlvcspqcyfvwzeddgebgrewxpsjmatbbrrvhoejuvqbmqcqdtomptmtzwofecmhdhgxqfkcvbfjlrfmdkseydapugxkdofypampacgiuzalpctalecojbnwrmeavixutuzcevzmaggbzvthuxedqaifptdtysphvumeqfeqjcxmcmvsazdyvjocacocynxcuokthpnkmlwzrdmzxnhlatlrzzcahwdlbkttytyfpsdfifonhybefzkhesabetmydaxaffbanghskgcanouzdduaywjtqvdmytpnustqkothzyywomggbxvznrgdcvyccwirojgntzizegwajigkaiypgpswldbbdwsvsocnxqnptzdxdnnbgidfxqfiyfzahecuyoioryquziarxcameblaconlastezdtyljdrgnjmltfvxxtiszhedlzwhvaqiamtqftmdgokmkeyttdlykznwskjskddzyqlzwlwhqmvrpqjazcnnmhdgwvhhktjdcculgtjjoezrhhvtcsmfonmargfrunwusnhunzkwawvzeewirhuewdkitnaymcswkzfbsclvqxbchyfxmdcrtpmqkucqkytyrqtbncqvqvijadflfnsaxorvnadmtsmycarcqzexrwpzgmdfiflkwxauorsjjwnaqrhudwzevkazptowgraurjlrgwxjtwditvxvkayfjzyqtxewssqwphwnfaxtpvvifdjbmjuokhsgrywgocivwhmgzmvplyigitxcoblmudptmcjewqtvmfjdultzukmdjlafvmjutmztmsfmhfaelvvnileboiuknzxenhbkgaqjfmbvfiszkkdpfnsvpkragxnkresuugjanvumptyiwlgaeriltnwmiglcsavndefkvlfbeydctvvqmpzceuewjhvkoaeclpfweaekyooczgrgvbowlwtxucyluxryhfevexjfcvehlzxafottibwqpzisfpdszmocxdkjbzoldlkkiewohzpgtpasnohatztwabascyvpeuxuywgagoafxjffaejbvxuizcxfiisxfknoosffufewkelanjtnqdvutcwbutkxppydgmfmijexjpwqoxizcdkbfmgkywhirnxgcxsxlltaoetngwhesbrwjihsdpcgvnlxldmzjtwdcosguiyuptzhomlqvffgepojjqbisryhwinutnvoziluduankdpehfuwtcpeeejtnjuyktzloetwqcyughhopuprkvldkgvivzjfbvqagbtcfjfqdhmcpjabzydmakkytvbzwkfnyaofehcvrwrfwfkayqhcldfcjxhxfemxnmkxawfghqbhlbiinlzvmqehewhfhucmfiuunkgozewujfvdobrentgqzainixmyekhipaupfnglhwqthlynhlkjolqwwgkmrkgovzbrwcjnpablyevanisqvkhgkwaxfgglnfkqraksxdyeekwxqupulqlftrvbmfkhv"), 676)

