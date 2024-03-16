# Пытался добавить **kwargs в __init__, но он представляет словарем, а по истории они пропали.
from primes_generator import prime_nums_generator


class MyDict:

    def __init__(self) -> None:
        self.__amount_of_buckets: int = 23
        self.__buckets: list = self.__init_buckets()
        self.__probation_step: int = 1
        self.__probation_quadratic_step: int = 3
        self.__deleted_counter: int = 0

        self.__prime_generator = prime_nums_generator()

        self.__deleted_mark = "deleted"

    def __init_buckets(self) -> list:
        return [None for _ in range(self.__amount_of_buckets)]

    def __iter__(self):
        for key in self.keys():
            yield key

    def __getitem__(self, key):
        value = self.__buckets[self.__get_bucket_number(key)]
        step = 0
        checked_indexes = set()
        while self.__check_is_real_value(value) and key != value[0]:
            step += 1
            bucket_number = self.__get_bucket_number(key, step)
            value = self.__buckets[bucket_number]
            if bucket_number in checked_indexes:
                value = None
                break

            checked_indexes.add(bucket_number)

        return value[1] if self.__check_is_real_value(value) else None

    def __contains__(self, key) -> bool:
        return bool(self[key])

    def __setitem__(self, key, value) -> None:
        step = 0
        checked_indexes = set()

        while self.__buckets[bucket_index := self.__get_bucket_number(key, step)]:
            step += 1

            if bucket_index in checked_indexes:
                self.__recreate_buckets()
            checked_indexes.add(bucket_index)

        self.__buckets[bucket_index] = (key, value)

    def __delitem__(self, key):
        step = 0
        bucket_number = self.__get_bucket_number(key)

        while value := self.__buckets[bucket_number]:
            if self.__check_is_real_value(value) and value[0] == key:
                self.__buckets[bucket_number] = self.__deleted_mark
                self.__deleted_counter += 1
                break
            step += 1
            bucket_number = self.__get_bucket_number(key, step)

        if self.__deleted_counter >= self.__amount_of_buckets // 2:
            self.__recreate_buckets()

    def __str__(self) -> str:
        return (
            "{\n    "
            + ",\n    ".join([f"{key}: {value}" for (key, value) in self.__get_valid_items()])
            + "\n}"
        )

    def __check_is_real_value(self, value) -> bool:
        return value is not None and value != self.__deleted_mark

    def __get_valid_items(self) -> list[tuple]:
        return list(filter(lambda x: x and x != self.__deleted_mark, self.__buckets))

    def __get_bucket_number(self, key, step: int = 0) -> int:
        return (
            hash(key) + step * self.__probation_step + step * self.__probation_quadratic_step ** 2
        ) % self.__amount_of_buckets

    def __recreate_buckets(self) -> None:
        while (prime := next(self.__prime_generator)) < self.__amount_of_buckets * 2:
            pass

        self.__amount_of_buckets = prime
        existing_items = self.__get_valid_items()
        self.__buckets = self.__init_buckets()

        for key, value in existing_items:
            self[key] = value

    def keys(self) -> list:
        return [item[0] for item in self.__get_valid_items()]

    def values(self) -> list:
        return [item[1] for item in self.__get_valid_items()]

    def items(self) -> list[tuple]:
        return self.__get_valid_items()


d = MyDict()
d["Alice"] = "random"
d["Hhih"] = "aaaa"
print("Alice" in d)
for i in range(20):
    d[i] = 'some_' + str(i)

print(d.keys())
print(d.values())
print(d.items())


for key in d:
    print(key)

for i in range(20):
    del d[i]

print(d)

del d["Alice"]
del d["Alice"]
print(d["Alice"])
print(d)
print("Alice" in d)
