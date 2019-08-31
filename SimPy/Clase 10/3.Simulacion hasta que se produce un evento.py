import simpy


def client(env):
    print('Start attention at %d' % env.now)
    yield env.timeout(4)
    print('Attended client at %d' % env.now)


def attention(env):
    yield env.process(client(env))


environment = simpy.Environment()
environment.run(environment.process(attention(environment)))
