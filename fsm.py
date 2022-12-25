from transitions.extensions import GraphMachine
from utils import send_multi_message
from linebot.models import *

class TocMachine(GraphMachine):

    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    # gaming
    def is_going_to_gaming(self, event):
        text = event.message.text
        if ((self.state == 'init' and text == '開始') or (self.state == 'resting' and text == '去打電動')):
            return True
    def on_enter_gaming(self, event):
        arr = []
        arr.append(
            TextSendMessage(text="遊戲開始\n杰哥不要互動遊戲,在這個遊戲中你將控制阿偉做出一連串正確的選擇 以逃過傑哥的魔掌 遊戲還有精彩的隱藏結局等著玩家去探索")
        )
        arr.append(
            ImageSendMessage(original_content_url='https://i.postimg.cc/LsQrnLHR/S-3088564.jpg', preview_image_url='https://i.postimg.cc/LsQrnLHR/S-3088564.jpg')
        )
        arr.append(
            TextSendMessage(text="你在家打電動，你被阿嬤罵了阿嬤叫你去讀書，你要?")
        )
        arr.append(
            TemplateSendMessage(
                alt_text='template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://i.postimg.cc/TwYgH5my/jjk.jpg',
                            action=PostbackTemplateAction(
                                label='煩欸',
                                text='煩欸',
                                data=' '
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://image.cache.storm.mg/styles/smg-800x533-fp/s3/media/image/2022/09/08/20220908-045510_U24553_M791985_d5bd.jpg',
                            action=PostbackTemplateAction(
                                label='去看書',
                                text='去看書',
                                data=' '
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://news3pic.cdn.org.tw/uploads/big/95ad1528477727397456242dcfd4e13c.jpg',
                            action=PostbackTemplateAction(
                                label='去休息',
                                text='去休息',
                                data=' '
                            )
                        ),
                    ]
                )
            )
        )
        send_multi_message(event.reply_token, arr)

    # resting
    def is_going_to_resting(self, event):
        text = event.message.text
        if ((self.state == 'gaming' and text == '去休息') or (self.state == 'resting' and text == '繼續休息')):
            return True
    def on_enter_resting(self, event):
        print("resting")
        arr = []
        arr.append(
            ImageSendMessage(original_content_url='https://news3pic.cdn.org.tw/uploads/big/95ad1528477727397456242dcfd4e13c.jpg', preview_image_url='https://news3pic.cdn.org.tw/uploads/big/95ad1528477727397456242dcfd4e13c.jpg')
        )
        arr.append(
            TextSendMessage(text="阿嬤讓你覺得很煩，所以你決定去休息不再打電動讓阿嬤閉嘴。你現在休息完。請問你要?")
        )
        arr.append(
            TemplateSendMessage(
                alt_text='template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://i.postimg.cc/LsQrnLHR/S-3088564.jpg',
                            action=MessageTemplateAction(
                                label='去打電動',
                                text='去打電動',
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://news3pic.cdn.org.tw/uploads/big/95ad1528477727397456242dcfd4e13c.jpg',
                            action=MessageTemplateAction(
                                label='繼續休息',
                                text='繼續休息',
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://image.cache.storm.mg/styles/smg-800x533-fp/s3/media/image/2022/09/08/20220908-045510_U24553_M791985_d5bd.jpg',
                            action=MessageTemplateAction(
                                label='去看書',
                                text='去看書',
                            )
                        ),
                    ]
                )
            )
        )
        send_multi_message(event.reply_token, arr)

    # goodend_study
    def is_going_to_goodend_study(self, event):
        text = event.message.text
        if ((self.state == 'gaming' and text == '去看書') or (self.state == 'resting' and text == '去看書') or (self.state == 'arguing' and text == '去看書')):
            return True
    def on_enter_goodend_study(self, event):
        print("goodend_study")
        arr = []
        arr.append(
            ImageSendMessage(
                original_content_url='https://image.cache.storm.mg/styles/smg-800x533-fp/s3/media/image/2017/04/28/20170428-024258_U3260_M274289_5146.jpg',
                preview_image_url= 'https://image.cache.storm.mg/styles/smg-800x533-fp/s3/media/image/2017/04/28/20170428-024258_U3260_M274289_5146.jpg'
            )
        )
        arr.append(
            TextSendMessage(text="好結局\n聽阿嬤的話乖乖去讀書成功考上建國中學")
        )
        send_multi_message(event.reply_token, arr)
        self.go_back()

    # arguing
    def is_going_to_arguing(self, event):
        text = event.message.text
        if ((self.state == 'gaming' and text == '煩欸')):
            return True
    def on_enter_arguing(self, event):
        print("arguing")
        arr = []
        arr.append(
	            ImageSendMessage(
		        original_content_url='https://i.postimg.cc/j2JzT0jP/ssss.jpg', 
		        preview_image_url='https://i.postimg.cc/j2JzT0jP/ssss.jpg'
	        )
        )
        arr.append(
	        TextSendMessage(text='阿嬤在一起旁邊一直煩你導致你的遊戲角色死掉了，阿嬤說他只是希望你可以好好用功讀書，你覺得很煩你現在決定?')
        )
        arr.append(
            TemplateSendMessage(
                alt_text='template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://truth.bahamut.com.tw/s01/202108/4aa9ed94d94f423e81c831e23acedb7e.JPG',
                            action=MessageTemplateAction(
                                label='找彬彬打咖',
                                text='找彬彬打咖',
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://image.cache.storm.mg/styles/smg-800x533-fp/s3/media/image/2022/09/08/20220908-045510_U24553_M791985_d5bd.jpg',
                            action=MessageTemplateAction(
                                label='去看書',
                                text='去看書',
                            )
                        ),
                    ]
                )
            )
        )
        send_multi_message(event.reply_token, arr)

    # internet_cafe
    def is_going_to_internet_cafe(self, event):
        text = event.message.text
        if ((self.state == 'arguing' and text == '找彬彬打咖') or (self.state == 'internet_cafe' and text == '我有多帶一點')):
            return True
    def on_enter_internet_cafe(self, event):
        print("internet_cafe")
        arr = []
        arr.append(
	            ImageSendMessage(
		        original_content_url='https://i.postimg.cc/ZBRfjfm4/play.jpg', 
		        preview_image_url='https://i.postimg.cc/ZBRfjfm4/play.jpg'
	        )
        )
        arr.append(
	        TextSendMessage(text='你和彬彬在網咖唱玩爆爆王玩得不亦樂乎，忽然網咖時數快到了，彬彬問你有沒有多帶一點錢?')
        )
        arr.append(
            TemplateSendMessage(
                alt_text='template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://i.postimg.cc/HrwPLc3D/money.jpg',
                            action=MessageTemplateAction(
                                label='我有多帶一點',
                                text='我有多帶一點',
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://i.postimg.cc/4KwLzDrW/nomoney.jpg',
                            action=MessageTemplateAction(
                                label='沒了喇，都花玩了',
                                text='沒了喇，都花玩了',
                            )
                        ),
                    ]
                )
            )
        )
        send_multi_message(event.reply_token, arr)

    # jay_bread
    def is_going_to_jay_bread(self, event):
        text = event.message.text
        if ((self.state == 'internet_cafe' and text == '沒了喇，都花玩了')):
            return True
    def on_enter_jay_bread(self, event):
        print("jay_bread")
        arr = []
        arr.append(
	            ImageSendMessage(
		        original_content_url='https://i.postimg.cc/23YFxkQT/hungery.jpg', 
		        preview_image_url='https://i.postimg.cc/23YFxkQT/hungery.jpg'
	        )
        )
        arr.append(
	            ImageSendMessage(
		        original_content_url='https://i.postimg.cc/KRvPd0sM/offering.jpg', 
		        preview_image_url='https://i.postimg.cc/KRvPd0sM/offering.jpg'
	        )
        )
        arr.append(
	        TextSendMessage(text='沒有錢就只能回家。你和彬彬沒有錢，所以走出了網咖在網咖門口，你們遇見一個自稱為杰哥的男人，聽到你們肚子很餓給了你們一塊麵包。請問你們要收香這塊麵包嗎？')
        )
        arr.append(
            TemplateSendMessage(
                alt_text='template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://i.postimg.cc/vgr7dksW/eat.jpg',
                            action=MessageTemplateAction(
                                label='吃',
                                text='吃',
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://i.postimg.cc/fkv72G5s/noteat.jpg',
                            action=MessageTemplateAction(
                                label='不吃',
                                text='不吃',
                            )
                        ),
                    ]
                )
            )
        )
        send_multi_message(event.reply_token, arr)

    # goodend_turn_down_jay
    def is_going_to_goodend_turn_down_jay(self, event):
        text = event.message.text
        if ((self.state == 'jay_bread' and text == '不吃') or (self.state == 'jay_invite' and text == '不去')):
            return True
    def on_enter_goodend_turn_down_jay(self, event):
        print("goodend_turn_down_jay")
        arr = []
        arr.append(
	            ImageSendMessage(
		        original_content_url='https://i2.hdslb.com/bfs/archive/4d10d2b857b13185609c40502be3c8d8a331d47f.jpg', 
		        preview_image_url='https://i2.hdslb.com/bfs/archive/4d10d2b857b13185609c40502be3c8d8a331d47f.jpg'
	        )
        )
        arr.append(
	        TextSendMessage(text='好結局\n機靈的你們感覺杰哥不是一個正常的人,因而拒絕他的邀約成功逃過一劫')
        )
        send_multi_message(event.reply_token, arr)
        self.go_back()


    # jay_invite
    def is_going_to_jay_invite(self, event):
        text = event.message.text
        if ((self.state == 'jay_bread' and text == '吃')):
            return True
    def on_enter_jay_invite(self, event):
        print("jay_invite")
        arr = []
        arr.append(
	            ImageSendMessage(
		        original_content_url='https://i.postimg.cc/WDjgwSrz/invite.jpg', 
		        preview_image_url='https://i.postimg.cc/WDjgwSrz/invite.jpg'
	        )
        )
        arr.append(
	        TextSendMessage(text='收下杰哥麵後，杰哥表示他時常幫助一些俏佳人。他家房子很大，你們可以來他家玩，而且等一下還會帶你們去超商買一些好吃的。請問你們要去嗎？')
        )
        arr.append(
            TemplateSendMessage(
                alt_text='template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://i.postimg.cc/WhBMhs1M/go.jpg',
                            action=MessageTemplateAction(
                                label='去',
                                text='去',
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://i.postimg.cc/TKnnbBKB/notgoing.jpg',
                            action=MessageTemplateAction(
                                label='不去',
                                text='不去',
                            )
                        ),
                    ]
                )
            )
        )
        send_multi_message(event.reply_token, arr)

    # market
    def is_going_to_market(self, event):
        text = event.message.text
        if ((self.state == 'jay_invite' and text == '去')):
            return True
    def on_enter_market(self, event):
        print("market")
        arr = []
        arr.append(
	            ImageSendMessage(
		        original_content_url='https://i.postimg.cc/4nJK2mmL/market.jpg', 
		        preview_image_url='https://i.postimg.cc/4nJK2mmL/market.jpg'
	        )
        )
        arr.append(
	        TextSendMessage(text='到了超市後你和彬彬走到飲料櫃前。彬彬想要買酒，你覺得應該要謹慎考慮。你認為該怎麼做?')
        )
        arr.append(
            TemplateSendMessage(
                alt_text='template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://i.postimg.cc/WF7dbPfw/drink.jpg',
                            action=MessageTemplateAction(
                                label='傑哥，這都可以拿嗎?',
                                text='傑哥，這都可以拿嗎?',
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://i.postimg.cc/H8sVrPqD/sober.jpg',
                            action=MessageTemplateAction(
                                label='不喝酒',
                                text='不喝酒',
                            )
                        ),
                    ]
                )
            )
        )
        send_multi_message(event.reply_token, arr)

    # goodend_staying_sober
    def is_going_to_goodend_staying_sober(self, event):
        text = event.message.text
        if ((self.state == 'market' and text == '不喝酒')):
            return True
    def on_enter_goodend_staying_sober(self, event):
        print("goodend_staying_sober")
        arr = []
        arr.append(
	            ImageSendMessage(
		        original_content_url='https://i2.hdslb.com/bfs/archive/4d10d2b857b13185609c40502be3c8d8a331d47f.jpg', 
		        preview_image_url='https://i2.hdslb.com/bfs/archive/4d10d2b857b13185609c40502be3c8d8a331d47f.jpg'
	        )
        )
        arr.append(
	        TextSendMessage(text='好結局\n你認為未成年不可以飲酒，所以就沒有買酒，因為你們沒有買酒，杰哥沒辦法把你們灌醉。你們成功逃過一劫')
        )
        send_multi_message(event.reply_token, arr)
        self.go_back()

    # jay_house
    def is_going_to_jay_house(self, event):
        text = event.message.text
        if ((self.state == 'market' and text == '傑哥，這都可以拿嗎?')):
            return True
    def on_enter_jay_house(self, event):
        print("jay_house")
        arr = []
        arr.append(
	            ImageSendMessage(
		        original_content_url='https://i.postimg.cc/bSgDwjdj/jayHome.jpg', 
		        preview_image_url='https://i.postimg.cc/bSgDwjdj/jayHome.jpg'
	        )
        )
        arr.append(
	        TextSendMessage(text='到了傑哥家以後冰冰已經快喝掛了請問你要繼續喝酒嗎？')
        )
        arr.append(
            TemplateSendMessage(
                alt_text='template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://i.postimg.cc/hX5mmgsD/drink.jpg',
                            action=MessageTemplateAction(
                                label='再喝',
                                text='再喝',
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://i.postimg.cc/Z0SwnF0f/stop.jpg',
                            action=MessageTemplateAction(
                                label='不喝',
                                text='不喝',
                            )
                        ),
                    ]
                )
            )
        )
        send_multi_message(event.reply_token, arr)


    # drink_once
    def is_going_to_drink_once(self, event):
        text = event.message.text
        if ((self.state == 'jay_house' and text == '再喝')):
            return True
    def on_enter_drink_once(self, event):
        print("drink_once")
        arr = []
        arr.append(
	            ImageSendMessage(
		        original_content_url='https://i.postimg.cc/bSgDwjdj/jayHome.jpg', 
		        preview_image_url='https://i.postimg.cc/bSgDwjdj/jayHome.jpg'
	        )
        )
        arr.append(
	        TextSendMessage(text='請問你要繼續喝酒嗎？')
        )
        arr.append(
            TemplateSendMessage(
                alt_text='template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://i.postimg.cc/hX5mmgsD/drink.jpg',
                            action=MessageTemplateAction(
                                label='再喝',
                                text='再喝',
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://i.postimg.cc/Z0SwnF0f/stop.jpg',
                            action=MessageTemplateAction(
                                label='不喝',
                                text='不喝',
                            )
                        ),
                    ]
                )
            )
        )
        send_multi_message(event.reply_token, arr)

    # drink_twice
    def is_going_to_drink_twice(self, event):
        text = event.message.text
        if ((self.state == 'drink_once' and text == '再喝')):
            return True
    def on_enter_drink_twice(self, event):
        print("drink_twice")
        arr = []
        arr.append(
	            ImageSendMessage(
		        original_content_url='https://i.postimg.cc/bSgDwjdj/jayHome.jpg', 
		        preview_image_url='https://i.postimg.cc/bSgDwjdj/jayHome.jpg'
	        )
        )
        arr.append(
	        TextSendMessage(text='請問你要繼續喝酒嗎？')
        )
        arr.append(
            TemplateSendMessage(
                alt_text='template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://i.postimg.cc/hX5mmgsD/drink.jpg',
                            action=MessageTemplateAction(
                                label='再喝',
                                text='再喝',
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://i.postimg.cc/Z0SwnF0f/stop.jpg',
                            action=MessageTemplateAction(
                                label='不喝',
                                text='不喝',
                            )
                        ),
                    ]
                )
            )
        )
        send_multi_message(event.reply_token, arr)

    # neutralend_drunk
    def is_going_to_neutralend_drunk(self, event):
        text = event.message.text
        if ((self.state == 'drink_twice' and text == '再喝')):
            return True
    def on_enter_neutralend_drunk(self, event):
        print("neutralend_drunk")
        arr = []
        arr.append(
	            ImageSendMessage(
		        original_content_url='https://i.postimg.cc/kGpfF3jp/binggetrape.png', 
		        preview_image_url='https://i.postimg.cc/kGpfF3jp/binggetrape.png'
	        )
        )
        arr.append(
	        TextSendMessage(text='壞結局\n你成功喝得比彬彬還要醉。傑哥喜歡吃活魚，看到你最醉那個樣子自討沒趣。而你的朋友冰冰就沒那麼幸運了。')
        )
        send_multi_message(event.reply_token, arr)
        self.go_back()

    # jay_tough
    def is_going_to_jay_tough(self, event):
        text = event.message.text
        if ((self.state == 'jay_house' and text == '不喝') or (self.state == 'drink_once' and text == '不喝') or (self.state == 'drink_twice' and text == '不喝')):
            return True
    def on_enter_jay_tough(self, event):
        print("jay_tough")
        arr = []
        arr.append(
	            ImageSendMessage(
		        original_content_url='https://i.postimg.cc/c6f5c1vL/jayaskiftouggh.jpg', 
		        preview_image_url='https://i.postimg.cc/c6f5c1vL/jayaskiftouggh.jpg'
	        )
        )
        arr.append(
	        TextSendMessage(text='你成功喝贏彬彬。看到彬彬醉倒，你也放下手中的杯子。杰哥看你這麼能喝就問你是不是很勇?')
        )
        arr.append(
            TemplateSendMessage(
                alt_text='template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://i.postimg.cc/bs8VVXnH/tough.jpg',
                            action=MessageTemplateAction(
                                label='我超勇的好不好啊。',
                                text='我超勇的好不好啊。',
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://i.postimg.cc/c6f5c1vL/jayaskiftouggh.jpg',
                            action=MessageTemplateAction(
                                label='我不勇。',
                                text='我不勇。',
                            )
                        ),
                    ]
                )
            )
        )
        send_multi_message(event.reply_token, arr)

    # jay_fit
    def is_going_to_jay_fit(self, event):
        text = event.message.text
        if ((self.state == 'jay_tough' and text == '我超勇的好不好啊。') or (self.state == 'jay_tough' and text == '我不勇。')):
            return True
    def on_enter_jay_fit(self, event):
        print("jay_fit")
        arr = []
        arr.append(
	            ImageSendMessage(
		        original_content_url='https://i.postimg.cc/GTP73KWy/fit.jpg', 
		        preview_image_url='https://i.postimg.cc/GTP73KWy/fit.jpg'
	        )
        )
        arr.append(
	        TextSendMessage(text='傑哥開始對你上下其手，抓了一下你的大腿')
        )
        arr.append(
            TemplateSendMessage(
                alt_text='template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://truth.bahamut.com.tw/s01/202011/767e0d11e1c49b049622a8eb5e71d9f8.JPG',
                            action=MessageTemplateAction(
                                label='傑哥，你幹嘛阿?',
                                text='傑哥，你幹嘛阿?',
                            )
                        )
                    ]
                )
            )
        )
        send_multi_message(event.reply_token, arr)

    # jay_youDoNotUnderstand
    def is_going_to_jay_youDoNotUnderstand(self, event):
        text = event.message.text
        if ((self.state == 'jay_fit' and text == '傑哥，你幹嘛阿?')):
            return True
    def on_enter_jay_youDoNotUnderstand(self, event):
        print("jay_youDoNotUnderstand")
        arr = []
        arr.append(
	            ImageSendMessage(
		        original_content_url='https://i.postimg.cc/Cz7ZkDYH/S-3088636.jpg', 
		        preview_image_url='https://i.postimg.cc/Cz7ZkDYH/S-3088636.jpg'
	        )
        )
        arr.append(
	        TextSendMessage(text='傑哥說你完全是都不懂？')
        )
        arr.append(
            TemplateSendMessage(
                alt_text='template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://i.postimg.cc/PLgNTQzh/S-3088638.jpg',
                            action=MessageTemplateAction(
                                label='懂甚麼阿',
                                text='懂甚麼阿',
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://i.imgur.com/2Bt4GPP.png',
                            action=MessageTemplateAction(
                                label='我懂了。',
                                text='我懂了。',
                            )
                        ),
                    ]
                )
            )
        )
        send_multi_message(event.reply_token, arr)

    # neutralend_consent
    def is_going_to_neutralend_consent(self, event):
        text = event.message.text
        if ((self.state == 'jay_youDoNotUnderstand' and text == '我懂了。') or (self.state == 'jay_blush' and text == '好') or (self.state == 'jay_letMeSee' and text == '好吧')):
            return True
    def on_enter_neutralend_consent(self, event):
        print("neutralend_consent")
        arr = []
        arr.append(
	            ImageSendMessage(
		        original_content_url='https://i.imgur.com/2Bt4GPP.png', 
		        preview_image_url='https://i.imgur.com/2Bt4GPP.png'
	        )
        )
        arr.append(
	            ImageSendMessage(
		        original_content_url='https://i.postimg.cc/c44zQGWx/wantmore.jpg', 
		        preview_image_url='https://i.postimg.cc/c44zQGWx/wantmore.jpg'
	        )
        )
        arr.append(
	        TextSendMessage(text='普通結局\n你半推半就地成全了杰哥。獻上的自己的第一次。')
        )
        send_multi_message(event.reply_token, arr)
        self.go_back()

    # jay_adult
    def is_going_to_jay_adult(self, event):
        text = event.message.text
        if ((self.state == 'jay_youDoNotUnderstand' and text == '懂甚麼阿')):
            return True
    def on_enter_jay_adult(self, event):
        print("jay_adult")
        arr = []
        arr.append(
	            ImageSendMessage(
		        original_content_url='https://i.postimg.cc/tZFJTn26/S-3088639.jpg', 
		        preview_image_url='https://i.postimg.cc/tZFJTn26/S-3088639.jpg'
	        )
        )
        arr.append(
	        TextSendMessage(text='傑哥表示可以教你登大人。')
        )
        arr.append(
            TemplateSendMessage(
                alt_text='template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://i.imgur.com/i8BIgsu.jpg',
                            action=MessageTemplateAction(
                                label='登大人?',
                                text='登大人?',
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://i.imgur.com/i8BIgsu.jpg',
                            action=MessageTemplateAction(
                                label='登大人??',
                                text='登大人?',
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://i.imgur.com/i8BIgsu.jpg',
                            action=MessageTemplateAction(
                                label='登大人???',
                                text='登大人?',
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://i.postimg.cc/wBVmCCC4/image.png',
                            action=MessageTemplateAction(
                                label='成功登大人',
                                text='成功登大人',
                            )
                        ),
                    ]
                )
            )
        )
        send_multi_message(event.reply_token, arr)

    # secretend_NCKU
    def is_going_to_secretend_NCKU(self, event):
        text = event.message.text
        if ((self.state == 'jay_adult' and text == '成功登大人')):
            return True
    def on_enter_secretend_NCKU(self, event):
        print("secretend_NCKU")
        arr = []
        arr.append(
	            ImageSendMessage(
		        original_content_url='https://i.postimg.cc/wBVmCCC4/image.png', 
		        preview_image_url='https://i.postimg.cc/wBVmCCC4/image.png'
	        )
        )
        arr.append(
	        TextSendMessage(text='隱藏結局\n國立成功大學是一所積極新創、學科齊全、學術實力雄厚、辦學特色鮮明，在國際上具有重要影響力與競爭力的綜合性大學，在多個學術領域具有非常前瞻的科技實力，擁有世界一流的實驗室與師資力量，各種排名均位於全球前列。歡迎大家報考國立成功大學。')
        )
        send_multi_message(event.reply_token, arr)
        self.go_back()

    # jay_porn
    def is_going_to_jay_porn(self, event):
        text = event.message.text
        if ((self.state == 'jay_adult' and text == '登大人?')):
            return True
    def on_enter_jay_porn(self, event):
        print("jay_porn")
        arr = []
        arr.append(
	            ImageSendMessage(
		        original_content_url='https://i.postimg.cc/MnSKXph2/goodstuff.png', 
		        preview_image_url='https://i.postimg.cc/MnSKXph2/goodstuff.png'
	        )
        )
        arr.append(
	        TextSendMessage(text='你跟著傑哥去的房間，傑哥給你看了奇怪的A片。')
        )
        arr.append(
            TemplateSendMessage(
                alt_text='template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://i.postimg.cc/gxHchPWw/whatis-This.png',
                            action=MessageTemplateAction(
                                label='傑哥，這是什麼啊?',
                                text='傑哥，這是什麼啊?',
                            )
                        )
                    ]
                )
            )
        )
        send_multi_message(event.reply_token, arr)

    # jay_blush
    def is_going_to_jay_blush(self, event):
        text = event.message.text
        if ((self.state == 'jay_porn' and text == '傑哥，這是什麼啊?')):
            return True
    def on_enter_jay_blush(self, event):
        print("jay_blush")
        arr = []
        arr.append(
	            ImageSendMessage(
		        original_content_url='', 
		        preview_image_url=''
	        )
        )
        arr.append(
	        TextSendMessage(text='')
        )
        arr.append(
            TemplateSendMessage(
                alt_text='template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://www.honhai.com/img/about/group-profile/founder-m.png?5f65a',
                            action=MessageTemplateAction(
                                label='好',
                                text='好',
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://www.honhai.com/img/about/group-profile/founder-m.png?5f65a',
                            action=MessageTemplateAction(
                                label='不要喇',
                                text='不要喇',
                            )
                        ),
                    ]
                )
            )
        )
        send_multi_message(event.reply_token, arr)

    # jay_letMeSee
    def is_going_to_jay_letMeSee(self, event):
        text = event.message.text
        if ((self.state == 'jay_blush' and text == '不要喇')):
            return True
    def on_enter_jay_letMeSee(self, event):
        print("jay_letMeSee")
        arr = []
        arr.append(
	            ImageSendMessage(
		        original_content_url='https://i.postimg.cc/tn9N7QQN/blush.png', 
		        preview_image_url='https://i.postimg.cc/tn9N7QQN/blush.png'
	        )
        )
        arr.append(
	        TextSendMessage(text='奇怪的A片讓你臉紅了，傑哥希望你能讓他看看。')
        )
        arr.append(
            TemplateSendMessage(
                alt_text='template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://i.postimg.cc/xcTP22P0/what-Youdoing-Jay.png',
                            action=MessageTemplateAction(
                                label='不要喇，傑哥，你幹嘛阿?',
                                text='不要喇，傑哥，你幹嘛阿?',
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://i.postimg.cc/nLKn5fPs/image.jpg',
                            action=MessageTemplateAction(
                                label='好吧',
                                text='好吧',
                            )
                        ),
                    ]
                )
            )
        )
        send_multi_message(event.reply_token, arr)

    # jay_ifYouAreNormal
    def is_going_to_jay_ifYouAreNormal(self, event):
        text = event.message.text
        if ((self.state == 'jay_letMeSee' and text == '不要喇，傑哥，你幹嘛阿?')):
            return True
    def on_enter_jay_ifYouAreNormal(self, event):
        print("jay_ifYouAreNormal")
        arr = []
        arr.append(
	            ImageSendMessage(
		        original_content_url='https://i.postimg.cc/bYk4994J/ifnormal.png', 
		        preview_image_url='https://i.postimg.cc/bYk4994J/ifnormal.png'
	        )
        )
        arr.append(
	        TextSendMessage(text='傑哥想要檢查你發育正不正常')
        )
        arr.append(
            TemplateSendMessage(
                alt_text='template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://i.postimg.cc/Fsxq2srX/jayno.png',
                            action=MessageTemplateAction(
                                label='好',
                                text='好',
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://i.postimg.cc/Fsxq2srX/jayno.png',
                            action=MessageTemplateAction(
                                label='傑哥，不要喇。',
                                text='傑哥，不要喇。',
                            )
                        ),
                    ]
                )
            )
        )
        send_multi_message(event.reply_token, arr)


    # jay_checked_your_body
    def is_going_to_jay_checked_your_body(self, event):
        text = event.message.text
        if ((self.state == 'jay_ifYouAreNormal' and text == '好')):
            return True
    def on_enter_jay_checked_your_body(self, event):
        print("jay_checked_your_body")
        arr = []
        arr.append(
	            ImageSendMessage(
		        original_content_url='https://i.postimg.cc/ZR7n7hW8/jjjjj.png', 
		        preview_image_url='https://i.postimg.cc/ZR7n7hW8/jjjjj.png'
	        )
        )
        arr.append(
	        TextSendMessage(text='傑哥檢查完你的身體，發現你發育?')
        )
        arr.append(
            TemplateSendMessage(
                alt_text='template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://i.postimg.cc/tJkKtX7b/good.png',
                            action=MessageTemplateAction(
                                label='發育良好。',
                                text='發育良好。',
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://postimg.cc/SJJD94Yg',
                            action=MessageTemplateAction(
                                label='發育正常。',
                                text='發育正常。',
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://attach.setn.com/newsimages/2021/01/06/2971804-PH.jpg',
                            action=MessageTemplateAction(
                                label='發育不正常',
                                text='發育不正常。',
                            )
                        ),
                    ]
                )
            )
        )
        send_multi_message(event.reply_token, arr)

    # goodend_too_small
    def is_going_to_goodend_too_small(self, event):
        text = event.message.text
        if ((self.state == 'jay_checked_your_body' and text == '發育不正常。')):
            return True
    def on_enter_goodend_too_small(self, event):
        print("goodend_too_small")
        arr = []
        arr.append(
	            ImageSendMessage(
		        original_content_url='https://i2.hdslb.com/bfs/archive/4d10d2b857b13185609c40502be3c8d8a331d47f.jpg', 
		        preview_image_url='https://i2.hdslb.com/bfs/archive/4d10d2b857b13185609c40502be3c8d8a331d47f.jpg'
	        )
        )
        arr.append(
	        TextSendMessage(text='好結局\n傑哥覺得你太小對你失去了興趣，你成功逃過一劫。')
        )
        send_multi_message(event.reply_token, arr)
        self.go_back()


    # jay_get_scared
    def is_going_to_jay_get_scared(self, event):
        text = event.message.text
        if ((self.state == 'jay_checked_your_body' and text == '發育良好。')):
            return True
    def on_enter_jay_get_scared(self, event):
        print("jay_get_scared")
        arr = []
        arr.append(
	            ImageSendMessage(
		        original_content_url='https://i.postimg.cc/bvKSpPyq/jay-Scared.png', 
		        preview_image_url='https://i.postimg.cc/bvKSpPyq/jay-Scared.png'
	        )
        )
        arr.append(
	        TextSendMessage(text='傑哥看到你那異於常人的大小感到害怕')
        )
        arr.append(
            TemplateSendMessage(
                alt_text='template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://i.postimg.cc/Y02rwDWp/reverse.png',
                            action=MessageTemplateAction(
                                label='我看你完全是不懂喔。',
                                text='我看你完全是不懂喔。',
                            )
                        ),
                    ]
                )
            )
        )
        send_multi_message(event.reply_token, arr)

    # secretend_reverse
    def is_going_to_secretend_reverse(self, event):
        text = event.message.text
        if ((self.state == 'jay_get_scared' and text == '我看你完全是不懂喔。')):
            return True
    def on_enter_secretend_reverse(self, event):
        print("secretend_reverse")
        arr = []
        arr.append(
	            ImageSendMessage(
		        original_content_url='https://i.postimg.cc/Y02rwDWp/reverse.png', 
		        preview_image_url='https://i.postimg.cc/Y02rwDWp/reverse.png'
	        )
        )
        arr.append(
	        TextSendMessage(text='隱藏結局\n你逆推了杰哥。')
        )
        send_multi_message(event.reply_token, arr)
        self.go_back()

    # jay_listen_letMeSee
    def is_going_to_jay_listen_letMeSee(self, event):
        text = event.message.text
        if ((self.state == 'jay_ifYouAreNormal' and text == '傑哥，不要喇。')):
            return True
    def on_enter_jay_listen_letMeSee(self, event):
        print("jay_listen_letMeSee")
        arr = []
        arr.append(
	            ImageSendMessage(
		        original_content_url='https://i.postimg.cc/3R5j9mDj/image.jpg', 
		        preview_image_url='https://i.postimg.cc/3R5j9mDj/image.jpg'
	        )
        )
        arr.append(
	        TextSendMessage(text='傑哥對你吼到: 聽話讓我看看!!!')
        )
        arr.append(
            TemplateSendMessage(
                alt_text='template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://i.imgur.com/Uc0zr1A.jpg',
                            action=MessageTemplateAction(
                                label='不要',
                                text='不要',
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://i.postimg.cc/qMXFKBSZ/image.jpg',
                            action=MessageTemplateAction(
                                label='邊哭邊脫下衣服。',
                                text='邊哭邊脫下衣服。',
                            )
                        ),
                    ]
                )
            )
        )
        send_multi_message(event.reply_token, arr)

    # jay_punch
    def is_going_to_jay_punch(self, event):
        text = event.message.text
        if ((self.state == 'jay_listen_letMeSee' and text == '不要')):
            return True
    def on_enter_jay_punch(self, event):
        print("jay_punch")
        arr = []
        arr.append(
	            ImageSendMessage(
		        original_content_url='https://i.postimg.cc/ft3TQkgG/punch.png', 
		        preview_image_url='https://i.postimg.cc/ft3TQkgG/punch.png'
	        )
        )
        arr.append(
	        TextSendMessage(text='傑哥奏了你一拳。')
        )
        arr.append(
            TemplateSendMessage(
                alt_text='template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://i.postimg.cc/wtjjFw5T/nonono.png',
                            action=MessageTemplateAction(
                                label='傑哥，不要喇。傑哥不要。',
                                text='傑哥，不要喇。傑哥不要。',
                            )
                        ),
                    ]
                )
            )
        )
        send_multi_message(event.reply_token, arr)

    # jay_took_of_cloth
    def is_going_to_jay_took_of_cloth(self, event):
        text = event.message.text
        if ((self.state == 'jay_punch' and text == '傑哥，不要喇。傑哥不要。')):
            return True
    def on_enter_jay_took_of_cloth(self, event):
        print("jay_took_of_cloth")
        arr = []
        arr.append(
	            ImageSendMessage(
		        original_content_url='https://i.postimg.cc/wtjjFw5T/nonono.png', 
		        preview_image_url='https://i.postimg.cc/wtjjFw5T/nonono.png'
	        )
        )
        arr.append(
	        TextSendMessage(text='傑哥拖了你的衣服。')
        )
        arr.append(
            TemplateSendMessage(
                alt_text='template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://i.postimg.cc/TwcPWtHF/image.jpg',
                            action=MessageTemplateAction(
                                label='傑哥。傑哥不要喇，傑哥',
                                text='傑哥。傑哥不要喇，傑哥',
                            )
                        ),
                    ]
                )
            )
        )
        send_multi_message(event.reply_token, arr)


    # jay_bed
    def is_going_to_jay_bed(self, event):
        text = event.message.text
        if ((self.state == 'jay_took_of_cloth' and text == '傑哥。傑哥不要喇，傑哥') or (self.state == 'jay_checked_your_body' and text == '發育正常。') or (self.state == 'jay_listen_letMeSee' and text == '邊哭邊脫下衣服。')):
            return True
    def on_enter_jay_bed(self, event):
        print("jay_bed")
        arr = []
        arr.append(
	            ImageSendMessage(
		        original_content_url='https://i.postimg.cc/DZNTtfnc/bed.png', 
		        preview_image_url='https://i.postimg.cc/DZNTtfnc/bed.png'
	        )
        )
        arr.append(
	        TextSendMessage(text='傑哥把你丟到床上。')
        )
        arr.append(
            TemplateSendMessage(
                alt_text='template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://i.postimg.cc/TwcPWtHF/image.jpg',
                            action=MessageTemplateAction(
                                label='傑哥不要!!!',
                                text='傑哥不要!!!',
                            )
                        ),
                    ]
                )
            )
        )
        send_multi_message(event.reply_token, arr)

    # badend_rape
    def is_going_to_badend_rape(self, event):
        text = event.message.text
        if ((self.state == 'jay_bed' and text == '傑哥不要!!!')):
            return True
    def on_enter_badend_rape(self, event):
        print("badend_rape")
        arr = []
        arr.append(
	            ImageSendMessage(
		        original_content_url='https://i.postimg.cc/Kz0PbVHf/noescape.jpg', 
		        preview_image_url='https://i.postimg.cc/Kz0PbVHf/noescape.jpg'
	        )
        )
        arr.append(
	        TextSendMessage(text='壞結局\n喔不!一系列錯誤的選擇讓你迎來的最糟糕的結局!被傑哥強上，如果找知道男生也會被性侵的話...')
        )
        send_multi_message(event.reply_token, arr)
        self.go_back()
