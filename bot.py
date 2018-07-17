from linepy import *


client = LINE()
client.log("Auth Token : " + str(client.authToken))

oepoll = OEPoll(client)

MySelf = client.getProfile()
JoinedGroups = client.getGroupIdsJoined()
print("My MID : " + MySelf.mid)

targets = []


def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        if op.param1 not in JoinedGroups:
                client.acceptGroupInvitation(op.param1)
                JoinedGroups.append(op.param1)
                client.sendMessage(op.param1, "✟ℓຫຼี้छゆຸ۞>_<")
  #  while True:
 #   try:
 #       ops = poll.singleTrace(count=50)
 #       if ops != None:
 #           for op in ops:
 #               if (op.type == 13):
 #                   client.acceptGroupInvitation(op.param1)
 #                   client.sendMessage(op.param1,'✟ℓຫຼี้छゆຸ۞>_<')                   
    except Exception as e:
        print(e)
        print("\n\nNOTIFIED_INVITE_INTO_GROUP\n\n")
        return
    
    
def SEND_MESSAGE(op):
    msg = op.message
    try:
        if msg.toType == 2:
            if msg.contentType == 0:
                if msg.text == "✟ℓຫຼี้छゆຸ۞>_<":
                    print("start destroying")
                    _name = msg.text.replace("✟ℓຫຼี้छゆຸ۞>_<","")
                    group = client.getGroup(msg.to)
                    targets = []
                    for g in group.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        client.leaveGroup(msg.to)
                        JoinedGroups.removm(msg.to)
                    else:
                        for target in targets:
                            group.name = "✟ℓຫຼี้छゆຸ۞>_<"
                            client.updateGroup(group)
                            try:                               
                if (op.type == 25):
                    msg = op.message
                    if (msg.text.lower() == 'start!'):
                        s = time.time()
                        client.sendMessage('Speed!')
                        e = time.time() - s
                        client.sendMessage('{:.14f}'.format(e))
                                client.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                               group.name = "✟ℓຫຼี้छゆຸ۞>_<"
                               client.updateGroup(group)
                               client.leaveGroup(msg.to)
                               JoinedGroups.remove(msg.to)
        else:
            pass
        
    except Exception as e:
        print(e)
        print("\n\nSEND_MESSAGE\n\n")
        return
    
oepoll.addOpInterruptWithDict({
    OpType.NOTIFIED_INVITE_INTO_GROUP: NOTIFIED_INVITE_INTO_GROUP,
    OpType.SEND_MESSAGE: SEND_MESSAGE
})


while True:
    oepoll.trace()
