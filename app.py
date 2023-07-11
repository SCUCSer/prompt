from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/question', methods=['POST'])
def handle_question():
    data = request.get_json()
    question = data['question']

    # 进行问题处理和匹配逻辑
    if question.isdigit():
        num_prompts = int(question)
        if num_prompts >= 0:
            prompts = generate_prompts(num_prompts)
            response = {
                'prompt': prompts
            }
        else:
            response = {
                'prompt': []
            }
    else:
        response = {
            'prompt': []
        }

    return jsonify(response)

def generate_prompts(num_prompts):
    prompts = []
    for _ in range(num_prompts):
        prompts.append(generate_random_prompt())
    return prompts

def generate_random_prompt():
    # 生成随机的prompt
    # 这里使用示例的字符串作为prompt，你可以根据实际需求进行修改
    prompts = [
        {
            'title': '搭乘「星穹铁道」，米哈游能再次改写二次元游戏格局吗？工业化路线下的“第二枚大棋”:《星穹铁道》要做的不只是游戏',
            'content': '《崩坏：星穹铁道》是一款战略角色扮演游戏，游戏并非开放世界，而是采用箱庭探索式的地图，以星球作为章节区域。世界各地存在多个“界域定锚”，可供玩家用于快速旅行[3]。玩家跟随游戏主线前往不同的地方，还有机关解密及支线任务等内容[4]。世界各地分布着奖励高价值资源的关卡，此类资源可以用于强化角色和购买道具，但需要消耗名为“开拓力”的体力才可进入，体力会随时间推移而缓慢回复[5][4]。另有名为“模拟宇宙”的Roguelike玩法可获得高级物资[6][7]。通过完成某些任务或参加特定的限时活动，玩家可解锁一些可玩角色[8]，但大多数角色都需通过名为“跃迁”抽卡系统获得[9]。游戏设有保底系统，玩家在抽取一定次数后必定获得稀有角色[10]。',
            'note': 'Prompt 1 Note'
        },
        {
            'title': 'Prompt 2 Title',
            'content': '《崩坏：星穹铁道》设定在一个科学幻想宇宙中[17]，银河中存在着星神，星神是一种高度凝聚的哲学概念化身，是那些践行某种信念并达到命途终点的人所成为的存在。星神掌握着改变现实和创造世界的力量，他们可以操控各自命途上的虚数能量。本作包含18种不同的命途，每个命途都代表了一种信念和力量，其中7种被设定为游戏中的角色职业。每个星神与其命途之间存在一种相互依存的关系。星神可以搬运命途上的能量，但同时也被命途所束缚。一旦命途开启，就无法关闭，即使星神陨落，命途仍然存在。目前已知的18位星神中，有一些已经陨落或失踪。',
            'note': 'Prompt 2 Note'
        },
        {
            'title': 'Prompt 3 Title',
            'content': '一日，反物质军团入侵空间站“黑塔”，卡芙卡和银狼趁乱潜入空间站，从中取出“星核”，将其注入作为“载体”的玩家角色“开拓者”（其名字和性别由玩家选择）体内。醒来的开拓者失去了记忆，卡芙卡告知开拓者将在未来开启冒险，而“在旅途的尽头，所有困扰你的谜题都将会解开”，两人随后离开。再次醒来后，开拓者遇到前来救援的“星穹列车”乘员三月七和丹恒，两人护送开拓者先后与防卫科负责人阿兰、星穹列车领航员姬子、空间站站长艾丝妲会面。一同消除了剩余的敌人后，由于体内“星核”的潜在威胁，开拓者在姬子以及空间站真正的主人黑塔的建议下，决定登上星穹列车，在无数“世界”与“世界”之间展开新的冒险，并解决星核对各个世界带来的威胁。',
            'note': '根据评论聚合网站Metacritic的数据，对《崩坏：星穹铁道》的评价以“正面评论为主”[42]。IGN的杰丝·雷耶斯（Jess Reyes）称其为2023年最好的免费开玩游戏[9]。许多评论家将其与《原神》相比较[45][43][9][44][48]，Eurogamer的杰茜卡·奥尔（Jessica Orr）将其归因于《原神》的受欢迎程度，她写道《崩坏：星穹铁道》是崩坏系列第四部作品，却被讨论得像是《原神》的续篇[43]。'
        },
        {
            'title': 'Prompt 4 Title',
            'content': '列车组的第一个目的地是雅利洛-Ⅵ，由于星核的影响，该星球大部分地区被寒潮覆盖。',
            'note': 'Prompt 4 Note'
        },
        {
            'title': 'Prompt 5 Title',
            'content': '《崩坏：星穹铁道》于2019年立项，目标是“为《崩坏》系列探索新方向”[2][19]，计划在上线后至少运营6年[1]。制作团队约为500名，大部分人是科幻作品和回合制角色扮演游戏的爱好者[18][1]。选择科幻题材是由于它是年轻一代所的期待内容[18]。该项目是米哈游首次尝试回合制战斗机制，团队认为该游戏类型在游戏市场很有吸引力，且能降低玩家的上手门槛[18]，在米哈游先前进行的问卷调查中，也有许多玩家表示喜欢该类型的游戏；对于此类型游戏是否过于复古的担忧，制作团队认为只要游戏质量足够便能吸引玩家[1]。《女神异闻录5》是团队想制作的回合制角色扮演游戏的目标，对团队选择制作该类游戏也有很大影响[2]。',
            'note': 'Prompt 5 Note'
        }
    ]
    return random.choice(prompts)

if __name__ == '__main__':
    app.run(debug=True)
