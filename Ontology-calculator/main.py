from Theory import Brain


test_sample = Brain("Test-0B")
test_sample.define_texture(0)


print(test_sample.get_texture())

test_sample.define_texture(2)

print(test_sample.get_texture())