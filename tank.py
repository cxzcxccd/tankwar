import  pygame,time,random
yanse=pygame.Color(0,0,0)
word_color=pygame.Color(255,0,0)
SCREEN_WIDTH=700
SCREEN_HEIGHT=500

class MainGame():
    window=None
    my_tank=None
    #创建敌方坦克
    enemytanklist=[]
    enemyct=5
    mybulletlist=[]


    def __init__(self):
        pass
    #开始游戏
    def startGame(self):
        ##加载主窗口
        pygame.display.init()
        ##设置窗口大小
        MainGame.window=pygame.display.set_mode([700,500])
        #初始化我的坦克
        MainGame.my_tank=Tank(350,250)
        #初始化敌方坦克
        self.createenemy()
        ##设置窗口标题
        pygame.display.set_caption("tankwar1.0")
        while True:
            #使坦克缓慢移动
            time.sleep(0.02)
            #给窗口填充色
            MainGame.window.fill(yanse)
            ##获取事件
            self.getEvent()
            ##绘制文字
            MainGame.window.blit(self.getword('敌方坦克剩余数量%d'%len(MainGame.enemytanklist)),(10,10))
            #调用坦克
            MainGame.my_tank.display()
            self.blitEnemytank()
            self.blitmybullet()
            #调用移动方法
            if not  MainGame.my_tank.stop:
              MainGame.my_tank.move()
            pygame.display.update()
    def createenemy(self):
        top=100
        for i in  range(MainGame.enemyct):
            left=random.randint(0,600)
            speed=random.randint(1,4)
            enemy=enemytank(left,top,speed)
            MainGame.enemytanklist.append(enemy)

    def blitEnemytank(self):
        for enemy in MainGame.enemytanklist:
            enemy.display()
            enemy.randmove()
    def blitmybullet(self):
        for mybbb in MainGame.mybulletlist:
            mybbb.displaybet()



    #结束游戏
    def endGame(self):
        print("感谢使用")
        exit()
    def getword(self,text):
        pygame.font.init()
        font=pygame.font.SysFont("kaiti",18)
        #绘制文本
        x=font.render(text,True,word_color)
        return x
    def getEvent(self):
        #获取所有事件
        evenList=pygame.event.get()
        #遍历事件
        for event in evenList:
            #判断按下的是否是关闭
              if  event.type==pygame.QUIT:
                  self.endGame()
              if   event.type==pygame.KEYDOWN:
                  ##判断上下作用
                    if event.key==pygame.K_UP:
                        #切换方向
                         MainGame.my_tank.direction='U'
                         MainGame.my_tank.stop=False
                         #MainGame.my_tank.move()
                         print("向上移动")
                    elif event.key==pygame.K_DOWN:
                          MainGame.my_tank.direction = 'D'
                          MainGame.my_tank.stop = False
                        #  MainGame.my_tank.move()
                          print("向下移动")
                    elif event.key == pygame.K_RIGHT:
                          MainGame.my_tank.direction = 'R'
                          MainGame.my_tank.stop = False
                        #  MainGame.my_tank.move()
                          print("向右移动")
                    elif event.key== pygame.K_LEFT:
                        MainGame.my_tank.direction = 'L'
                        MainGame.my_tank.stop = False
                       # MainGame.my_tank.move()
                        print("向左移动")
                    elif event.key==pygame.K_SPACE:
                        print("开炮")
                        bbb=bullet(MainGame.my_tank)
                        MainGame.mybulletlist.append(bbb)
                 # 松开时
              if event.type == pygame.KEYUP:
                  #判断松开的是什么
                  if event.key==pygame.K_UP or event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==pygame.K_DOWN:
                     MainGame.my_tank.stop= True


    #坦克
class  Tank():
    #添加距离左边left 距离上边top
    def __init__(self,left,top):
        #保存加载的图片
        self.images={
            'D': pygame.image.load('resources/images/hero/hero1D.gif'),
            'L': pygame.image.load('resources/images/hero/hero1L.gif'),
            'R': pygame.image.load('resources/images/hero/hero1R.gif'),
            'U': pygame.image.load('resources/images/hero/hero1U.gif')
                     }
        #移动
        self.direction='L'
        #根据当前图片的方向获取图片
        self.image=self.images[self.direction]
        #区域
        self.rect=self.image.get_rect()
        #设置区域的left  top
        self.rect.left=left
        self.rect.top=top
        self.speed=10
        self.stop=True
        self.step = 60
    def move(self):
        #判断direc
        if self.direction=='L':
            if self.rect.left>0:
              self.rect.left-=self.speed
        elif self.direction=='U':
            if self.rect.top>0:
              self.rect.top-=self.speed
        elif self.direction=='D':
            if self.rect.top+self.rect.height<500:
              self.rect.top+=self.speed
        elif self.direction=='R':
            if self.rect.left+self.rect.height<700:
              self.rect.left+=self.speed
    def shot(self):
        pass
    def display(self):
        #调用blit方法展示
        self.image=self.images[self.direction]
        MainGame.window.blit(self.image,self.rect)





    #我方坦克
class  MyTank(Tank):
    def __init__(self):
        pass





    #敌方坦克
class enemytank(Tank):
    def __init__(self,left,top,speed):
        #加载图片集
        self.images={
            'D': pygame.image.load('resources/images/enemy/enemy1D.gif'),
            'L': pygame.image.load('resources/images/enemy/enemy1L.gif'),
            'R': pygame.image.load('resources/images/enemy/enemy1R.gif'),
            'U': pygame.image.load('resources/images/enemy/enemy1U.gif')
        }
        self.direction=self.randDirection()
        self.image=self.images[self.direction]
        self.rect=self.image.get_rect()
        self.rect.left=left
        self.rect.top=top
        self.speed=speed
        self.stop=True
        self.step = 60


    def randDirection(self):
        num=random.randint(1,4)
        if num==1:
            return 'U'
        elif num==2:
            return 'D'
        elif num==3:
            return 'L'
        elif num==4:
            return 'R'
    def randmove(self):
        if self.step <= 0:
           self.direction = self.randDirection()
           self.step = 60
        else :
            self.move()
            self.step-=1







    #子弹类
class bullet():
    def __init__(self,tank):
        self.image=pygame.image.load('resources/images/bullet/bullet.gif.gif')
        #子弹的方向和坦克的方向是有关系的
        self.direction=tank.direction
        self.rect=self.image.get_rect()
        if self.direction=='U':
            self.rect.left=+tank.rect.left+tank.rect.width/2-self.rect.width/2
            self.rect.top=tank.rect.top-self.rect.height
        elif self.direction=='D':
           self.rect.left=tank.rect.left+tank.rect.width/2-self.rect.width/2
           self.rect.top=tank.rect.top+tank.rect.height
        elif self.direction=='L':
            self.rect.top=tank.rect.left-self.rect.width/2-self.rect.width/2
            self.rect.top=tank.rect.top+tank.rect.width/2-self.rect.width/2
        elif self.direction=='R':
            self.rect.left=tank.rect.left+tank.rect.width
            self.rect.top=tank.rect.top+tank.rect.width/2-self.rect.width/2
        self.speed=5
    def move(self):
        if self.direction=='U':
            if self.rect.top>0:
                self.rect.top-=self.speed
            else:
                pass
        elif self.direction=='R':
            if self.rect.left+self.rect.width<SCREEN_WIDTH:
                self.rect.left+=self.speed
            else:
                pass
        elif self.direction == 'D':
            if self.rect.top+self.rect.height<SCREEN_HEIGHT:
                self.rect.top+=self.speed
        elif self.direction == 'L':



    def displaybet(self):
        MainGame.window.blit(self.image,self.rect)


    #墙类
class wall():
    def __init__(self):
        pass
    #展示墙壁
    def displayWall(self):
        pass








    #爆炸类
class Explode():
    def __init__(self):
        pass
    def displayboom(self):
        pass




    #音乐类
class music():
    def __init__(self):
        pass



if __name__=='__main__':
    MainGame().startGame()