#coding:utf-8
'''
用于迭代计算V_star
案例是吴恩达的视频提供的数据
这里是值迭代,异步迭代
学习使用git
学写类
'''
import matplotlib.pyplot as plt

#初始化所有的v(s),vs[2][4] vs[3][4]接下来不更新,vs[2][2]也不更新（可以理解为柱子）
class RL(object):
    def __init__(self,i):
        self.i = i

    def max_cal_sum_pv(self,j,k,vs):
        value = 0

        if j+1==1 and k+1==1:
            value_N = 0.8*vs[j][k+1]+0.1*vs[j][k]+0.1*vs[j+1][k]
            value_E = 0.8*vs[j+1][k]+0.1*vs[j][k]+0.1*vs[j][k+1]
            value = max(value_N,value_E)
        elif j+1==1 and k+1==2:
            value_N = 0.8*vs[j][k+1]+0.1*vs[j][k]+0.1*vs[j][k]
            value_S = 0.8*vs[j][k]+0.1*vs[j][k]+0.1*vs[j][k]
            value = max(value_N,value_S)
        elif j+1==1 and k+1==3:
            value_E = 0.8*vs[j+1][k]+0.1*vs[j][k]+0.1*vs[j][k-1]
            value_S = 0.8*vs[j][k-1]+0.1*vs[j][k]+0.1*vs[j+1][k]
            value = max(value_E,value_S)
        elif j+1==2 and k+1==1:
            value_W = 0.8*vs[j-1][k]+0.1*vs[j][k]+0.1*vs[j][k]
            value_E = 0.8*vs[j+1][k]+0.1*vs[j][k]+0.1*vs[j][k]
            value = max(value_W,value_E)
        elif j+1==2 and k+1==3:
            value_W = 0.8*vs[j-1][k]+0.1*vs[j][k]+0.1*vs[j][k]
            value_E = 0.8*vs[j+1][k]+0.1*vs[j][k]+0.1*vs[j][k]
            value = max(value_W,value_E)  
        elif j+1==3 and k+1==1:
            value_N = 0.8*vs[j][k+1]+0.1*vs[j-1][k]+0.1*vs[j+1][k]
            value_W = 0.8*vs[j-1][k]+0.1*vs[j][k]+0.1*vs[j][k+1]
            value_E = 0.8*vs[j+1][k]+0.1*vs[j][k]+0.1*vs[j][k+1]
            value = max(value_W,value_E)
            value = max(value,value_N)
        elif j+1==3 and k+1==2:
            value_N = 0.8*vs[j][k+1]+0.1*vs[j][k]+0.1*vs[j+1][k]
            value_S = 0.8*vs[j][k-1]+0.1*vs[j][k]+0.1*vs[j+1][k]
            value_E = 0.8*vs[j+1][k]+0.1*vs[j][k+1]+0.1*vs[j][k-1]
            value = max(value_S,value_E)
            value = max(value,value_N)
        elif j+1==3 and k+1==3:
            value_S = 0.8*vs[j][k-1]+0.1*vs[j-1][k]+0.1*vs[j+1][k]
            value_W = 0.8*vs[j-1][k]+0.1*vs[j][k]+0.1*vs[j][k-1]
            value_E = 0.8*vs[j+1][k]+0.1*vs[j][k]+0.1*vs[j][k-1]
            value = max(value_S,value_E)
            value = max(value,value_W)
        elif j+1==4 and k+1==1:
            value_N = 0.8*vs[j][k+1]+0.1*vs[j][k]+0.1*vs[j-1][k]
            value_W = 0.8*vs[j-1][k]+0.1*vs[j][k]+0.1*vs[j][k+1]
            value = max(value_N,value_W)
        else:
            pass


        return value

    def val_iteration(self):
        RS=-0.02
        GAMMA=0.99
        vs=[[0,0,0],[0,0,0],[0,0,0],[0,-1,1]]
        for i in range(self.i):
            for j in range(4):
                # print "j=",j
                for k in range(3):
                    # print "k=",k
                    if not ((j+1==2 and k+1==2)or(j+1==4 and k+1==2)or(j+1==4 and k+1==3)):
                        # print j,"   ",k
                        vs[j][k] =  RS +GAMMA*self.max_cal_sum_pv(j,k,vs)

                    plt.plot(i,vs[0][0],'*-')
        plt.savefig("./examples.jpg") 


        print (vs)
        return vs

    def cal_pi_star(self,vs):
        pi_star = list()
        for i in range(4):#列
            for j in range(3):#行
                if i+1==1 and j+1==1:
                    pi_star_N = 0.8*vs[i][j+1]+0.1*vs[i][j]+0.1*vs[i+1][j]
                    pi_star_W = 0.8*vs[i][j]+0.1*vs[i][j+1]+0.1*vs[i][j]
                    pi_star_E = 0.8*vs[i+1][j]+0.1*vs[i][j]+0.1*vs[i][j]
                    pi_star_S = 0.8*vs[i][j]+0.1*vs[i][j]+0.1*vs[i+1][j]
                    pi_star_max = max(pi_star_N,pi_star_W,pi_star_E,pi_star_S)
                    if pi_star_max==pi_star_N:
                        pi_star.append("N")
                    elif pi_star_max ==pi_star_E:
                        pi_star.append("E")
                    elif pi_star_max ==pi_star_W:
                        pi_star.append("W")
                    else:
                        pi_star.append("S")

                elif i+1==1 and j+1==2:
                    pi_star_N = 0.8*vs[i][j+1]+0.1*vs[i][j]+0.1*vs[i][j]
                    pi_star_W = 0.8*vs[i][j]+0.1*vs[i][j+1]+0.1*vs[i][j-1]
                    pi_star_E = 0.8*vs[i][j]+0.1*vs[i][j+1]+0.1*vs[i][j-1]
                    pi_star_S = 0.8*vs[i][j-1]+0.1*vs[i][j]+0.1*vs[i][j]
                    pi_star_max = max(pi_star_N,pi_star_W,pi_star_E,pi_star_S)
                    if pi_star_max==pi_star_N:
                        pi_star.append("N")
                    elif pi_star_max ==pi_star_E:
                        pi_star.append("E")
                    elif pi_star_max ==pi_star_W:
                        pi_star.append("W")
                    else:
                        pi_star.append("S")

                elif i+1==1 and j+1==3:
                    pi_star_N = 0.8*vs[i][j]+0.1*vs[i][j]+0.1*vs[i+1][j]
                    pi_star_W = 0.8*vs[i][j]+0.1*vs[i][j-1]+0.1*vs[i][j]
                    pi_star_E = 0.8*vs[i+1][j]+0.1*vs[i][j]+0.1*vs[i][j]
                    pi_star_S = 0.8*vs[i][j-1]+0.1*vs[i][j]+0.1*vs[i+1][j]
                    pi_star_max = max(pi_star_N,pi_star_W,pi_star_E,pi_star_S)
                    if pi_star_max==pi_star_N:
                        pi_star.append("N")
                    elif pi_star_max ==pi_star_E:
                        pi_star.append("E")
                    elif pi_star_max ==pi_star_W:
                        pi_star.append("W")
                    else:
                        pi_star.append("S")

                elif i+1==2 and j+1==1:
                    pi_star_N = 0.8*vs[i][j]+0.1*vs[i-1][j]+0.1*vs[i+1][j]
                    pi_star_W = 0.8*vs[i-1][j]+0.1*vs[i][j]+0.1*vs[i][j]
                    pi_star_E = 0.8*vs[i+1][j]+0.1*vs[i][j]+0.1*vs[i][j]
                    pi_star_S = 0.8*vs[i][j]+0.1*vs[i-1][j]+0.1*vs[i+1][j]
                    pi_star_max = max(pi_star_N,pi_star_W,pi_star_E,pi_star_S)
                    if pi_star_max==pi_star_N:
                        pi_star.append("N")
                    elif pi_star_max ==pi_star_E:
                        pi_star.append("E")
                    elif pi_star_max ==pi_star_W:
                        pi_star.append("W")
                    else:
                        pi_star.append("S")

                elif i+1==2 and j+1==2:
                    pi_star.append("0")

                elif i+1==2 and j+1==3:
                    pi_star_N = 0.8*vs[i][j]+0.1*vs[i-1][j]+0.1*vs[i+1][j]
                    pi_star_W = 0.8*vs[i-1][j]+0.1*vs[i][j]+0.1*vs[i][j]
                    pi_star_E = 0.8*vs[i+1][j]+0.1*vs[i][j]+0.1*vs[i][j]
                    pi_star_S = 0.8*vs[i][j]+0.1*vs[i-1][j]+0.1*vs[i+1][j]
                    pi_star_max = max(pi_star_N,pi_star_W,pi_star_E,pi_star_S)
                    if pi_star_max==pi_star_N:
                        pi_star.append("N")
                    elif pi_star_max ==pi_star_E:
                        pi_star.append("E")
                    elif pi_star_max ==pi_star_W:
                        pi_star.append("W")
                    else:
                        pi_star.append("S")
                elif i+1==3 and j+1==1:
                    pi_star_N = 0.8*vs[i][j+1]+0.1*vs[i-1][j]+0.1*vs[i+1][j]
                    pi_star_W = 0.8*vs[i-1][j]+0.1*vs[i][j]+0.1*vs[i][j+1]
                    pi_star_E = 0.8*vs[i+1][j]+0.1*vs[i][j]+0.1*vs[i][j+1]
                    pi_star_S = 0.8*vs[i][j]+0.1*vs[i-1][j]+0.1*vs[i+1][j]
                    pi_star_max = max(pi_star_N,pi_star_W,pi_star_E,pi_star_S)
                    if pi_star_max==pi_star_N:
                        pi_star.append("N")
                    elif pi_star_max ==pi_star_E:
                        pi_star.append("E")
                    elif pi_star_max ==pi_star_W:
                        pi_star.append("W")
                    else:
                        pi_star.append("S")
                elif i+1==3 and j+1==2:
                    pi_star_N = 0.8*vs[i][j+1]+0.1*vs[i][j]+0.1*vs[i+1][j]
                    pi_star_W = 0.8*vs[i][j]+0.1*vs[i][j+1]+0.1*vs[i][j-1]
                    pi_star_E = 0.8*vs[i+1][j]+0.1*vs[i][j+1]+0.1*vs[i][j-1]
                    pi_star_S = 0.8*vs[i][j-1]+0.1*vs[i][j]+0.1*vs[i+1][j]
                    pi_star_max = max(pi_star_N,pi_star_W,pi_star_E,pi_star_S)
                    if pi_star_max==pi_star_N:
                        pi_star.append("N")
                    elif pi_star_max ==pi_star_E:
                        pi_star.append("E")
                    elif pi_star_max ==pi_star_W:
                        pi_star.append("W")
                    else:
                        pi_star.append("S")
                elif i+1==3 and j+1==3:
                    pi_star_N = 0.8*vs[i][j]+0.1*vs[i-1][j]+0.1*vs[i+1][j]
                    pi_star_W = 0.8*vs[i-1][j]+0.1*vs[i][j]+0.1*vs[i][j-1]
                    pi_star_E = 0.8*vs[i+1][j]+0.1*vs[i][j]+0.1*vs[i][j-1]
                    pi_star_S = 0.8*vs[i][j-1]+0.1*vs[i-1][j]+0.1*vs[i+1][j]
                    pi_star_max = max(pi_star_N,pi_star_W,pi_star_E,pi_star_S)
                    if pi_star_max==pi_star_N:
                        pi_star.append("N")
                    elif pi_star_max ==pi_star_E:
                        pi_star.append("E")
                    elif pi_star_max ==pi_star_W:
                        pi_star.append("W")
                    else:
                        pi_star.append("S")

                elif i+1==4 and j+1==1:
                    pi_star_N = 0.8*vs[i][j+1]+0.1*vs[i][j]+0.1*vs[i-1][j]
                    pi_star_W = 0.8*vs[i-1][j]+0.1*vs[i][j]+0.1*vs[i][j+1]
                    pi_star_E = 0.8*vs[i][j]+0.1*vs[i][j+1]+0.1*vs[i][j]
                    pi_star_S = 0.8*vs[i][j]+0.1*vs[i][j]+0.1*vs[i-1][j]
                    pi_star_max = max(pi_star_N,pi_star_W,pi_star_E,pi_star_S)
                    if pi_star_max==pi_star_N:
                        pi_star.append("N")
                    elif pi_star_max ==pi_star_E:
                        pi_star.append("E")
                    elif pi_star_max ==pi_star_W:
                        pi_star.append("W")
                    else:
                        pi_star.append("S")

                elif i+1==4 and j+1==2:
                    pi_star.append("-1")
                else:
                    pi_star.append("+1")

        print (pi_star)


def main():
    a = RL(100)
    vs = a.val_iteration()#计算V_STAR
    a.cal_pi_star(vs)#计算最佳策略


if __name__=="__main__":
    main()
