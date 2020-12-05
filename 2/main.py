if __name__ == '__main__':
    tab = [int(i) for i in input().split()]
    tab_2, sub_tab, k = [], [], 0
    case = tab[0]
    for i in tab:
        if i >= case:
            sub_tab.append(i)
        else:
            tab_2.append(sub_tab)
            sub_tab = [i]
        case = i
    for i in tab_2:
        if len(i) > 1:
            print(*i[::-1], end=' ')
            k += 1
        else:
            print(*i,  end=' ')
    print(k)
