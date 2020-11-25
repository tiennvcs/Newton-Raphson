import numpy as np
import os
import argparse
import matplotlib.pyplot as plt
from get_values import get_values



def get_argument():
    parser = argparse.ArgumentParser(description="Solve equation system using Newton-Raphson")
    parser.add_argument("-T2", help="Nhiệu độ vừng khử", type=int, default=750.0)   # 750, 800, 850, 900
    return parser.parse_args()


def plot_graphs(path: str, T2: float):

    LHVs, n1_percents, n2_percents, n3_percents, n4_percents, n6_percents = get_values(path=path,T2=T2)
    ER = np.array([0.2, 0.25, 0.3, 0.35, 0.4])
    fig, axes = plt.subplots(figsize=(7, 5))
    # print(matrix[:, 0])
    # expected_1 = getExpectation(solution=matrix[:, 0])
    ln1 = axes.plot(ER, n1_percents, '^-', label='C', linewidth=1)
    ln2 = axes.plot(ER, n2_percents, 'o-', label=r'$H_2$', linewidth=1)
    ln3 = axes.plot(ER, n3_percents, 's-', label='CO', linewidth=1)
    ln4 = axes.plot(ER, n4_percents, 'x-', label='$CO_2$', linewidth=1)
    ln5 = axes.plot(ER, n6_percents, 'd--', label='$CH_4$', linewidth=1)

    #axes.scatter(ER, n1_percents, marker='s', color='r')
    axes.text(ER[0], n1_percents[0]+0.5, r'${}$'.format(round(n1_percents[0],2 )), fontsize=8)
    axes.text(ER[1], n1_percents[1]+0.5, r'${}$'.format(round(n1_percents[1],2 )), fontsize=8)
    axes.text(ER[2], n1_percents[2]+0.5, r'${}$'.format(round(n1_percents[2],2 )), fontsize=8)
    axes.text(ER[3], n1_percents[3]+0.5, r'${}$'.format(round(n1_percents[3],2 )), fontsize=8)
    axes.text(ER[4], n1_percents[4]+0.5, r'${}$'.format(round(n1_percents[4],2 )), fontsize=8)

    #axes.scatter(ER, n2_percents, marker='D', color='g')
    axes.text(ER[0], n2_percents[0]+0.5, r'${}$'.format(round(n2_percents[0],2 )), fontsize=8)
    axes.text(ER[1], n2_percents[1]+0.5, r'${}$'.format(round(n2_percents[1],2 )), fontsize=8)
    axes.text(ER[2], n2_percents[2]+0.5, r'${}$'.format(round(n2_percents[2],2 )), fontsize=8)
    axes.text(ER[3], n2_percents[3]+0.5, r'${}$'.format(round(n2_percents[3],2 )), fontsize=8)
    axes.text(ER[4], n2_percents[4]+0.5, r'${}$'.format(round(n2_percents[4],2 )), fontsize=8)

    #axes.scatter(ER, n3_percents, marker='X', color='c')
    axes.text(ER[0], n3_percents[0]+0.5, r'${}$'.format(round(n3_percents[0],2 )), fontsize=8)
    axes.text(ER[1], n3_percents[1]+0.5, r'${}$'.format(round(n3_percents[1],2 )), fontsize=8)
    axes.text(ER[2], n3_percents[2]+0.5, r'${}$'.format(round(n3_percents[2],2 )), fontsize=8)
    axes.text(ER[3], n3_percents[3]+0.5, r'${}$'.format(round(n3_percents[3],2 )), fontsize=8)
    axes.text(ER[4], n3_percents[4]+0.5, r'${}$'.format(round(n3_percents[4],2 )), fontsize=8)

    #axes.scatter(ER, n4_percents, marker='d', color='b')
    axes.text(ER[0], n4_percents[0]+0.5, r'${}$'.format(round(n4_percents[0],2 )), fontsize=8)
    axes.text(ER[1], n4_percents[1]+0.5, r'${}$'.format(round(n4_percents[1],2 )), fontsize=8)
    axes.text(ER[2], n4_percents[2]+0.5, r'${}$'.format(round(n4_percents[2],2 )), fontsize=8)
    axes.text(ER[3], n4_percents[3]+0.5, r'${}$'.format(round(n4_percents[3],2 )), fontsize=8)
    axes.text(ER[4], n4_percents[4]+0.5, r'${}$'.format(round(n4_percents[4],2 )), fontsize=8)

    #axes.scatter(ER, n6_percents, marker='*', color='y')
    axes.text(ER[0], n6_percents[0]-1, r'${}$'.format(round(n6_percents[0],2 )), fontsize=8)
    axes.text(ER[1], n6_percents[1]-1, r'${}$'.format(round(n6_percents[1],2 )), fontsize=8)
    axes.text(ER[2], n6_percents[2]-1, r'${}$'.format(round(n6_percents[2],2 )), fontsize=8)
    axes.text(ER[3], n6_percents[3]-1, r'${}$'.format(round(n6_percents[3],2 )), fontsize=8)
    axes.text(ER[4], n6_percents[4]-1, r'${}$'.format(round(n6_percents[4],2 )), fontsize=8)


    
    axes.set_xlabel("ER", fontsize=10)
    axes.set_ylabel("Syngas Compositions (%)", fontsize=10)
    axes.set_ylim(0)
    
    ax2 = axes.twinx()  # instantiate a second axes that shares the same x-axis
    ax2.set_ylabel(r'LHV (kcal/N$m^3$)', color='tab:red')  # we already handled the x-label with ax1
    ln6 = ax2.plot(ER, LHVs, 'x-', linewidth=2, label='LHV', color='tab:red')
    ax2.text(ER[0], LHVs[0]-55, r'${}$'.format(round(LHVs[0],2)), fontsize=8)
    ax2.text(ER[1], LHVs[1]-55, r'${}$'.format(round(LHVs[1],2)), fontsize=8)
    ax2.text(ER[2], LHVs[2]-55, r'${}$'.format(round(LHVs[2],2)), fontsize=8)
    ax2.text(ER[3], LHVs[3]-55, r'${}$'.format(round(LHVs[3],2)), fontsize=8)
    ax2.text(ER[4], LHVs[4]-55, r'${}$'.format(round(LHVs[4],2)), fontsize=8)
    ax2.tick_params(axis='y', labelcolor='tab:red')
    ax2.set_ylim(0, np.max(LHVs)+100)
    
    # ax2.set_yticks(y_pos)
    # ax2.set_yticklabels(people)

    axes.set_xticks(ER)
    axes.set_title(str(int(T2)) + r"$^{o} C$", fontsize=12)
    plt.grid(True, linestyle =':')
    
    #plt.legend(bbox_to_anchor=(0.5, -0.1), loc='lower center', borderaxespad=0.)
    lns = ln1+ln2+ln3+ln4+ln5+ln6
    labs = [l.get_label() for l in lns]
    axes.legend(bbox_to_anchor=(0.5, -0.3), loc="lower center", ncol=6, handles=lns, labels=labs)
    #ax2.legend(bbox_to_anchor=(0.5, -0.5), loc="lower center", ncol=1)
    plt.subplots_adjust(bottom=0.25)
    plt.show()


if __name__ == '__main__':
    args = get_argument()
    path = "output_solutions"
    plot_graphs(path=path, T2=float(args.T2))
