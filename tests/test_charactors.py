from diceutils.charactors import TemplateManager, Attribute, AttributeGroup


def test_charactor():
    manager = TemplateManager()

    manager.add_template(
        "COC",
        [
            AttributeGroup(
                "个人信息",
                [
                    Attribute("name", str, ["名字", "称谓"]),
                    Attribute("sex", str, ["gender", "sex"]),
                    Attribute("age", int, ["age"]),
                    Attribute("edu_expr", list, ["学历"]),
                    Attribute("job", list, ["职业"]),
                ],
            ),
            AttributeGroup("技能", [Attribute("侦查", int, ["侦察"])]),
        ],
    )

    coc_card_data = {"sex": "男", "age": 22, "侦查": 50, "test": 1}
    coc_card = manager.build_card("coc")
    coc_card.plain_loads(coc_card_data)  # plain_loads是原本的import方法
    assert coc_card.get("age") == 22

    assert coc_card.dumps() == coc_card_data  # dumps是原来的export方法

    coc_card.loads(coc_card_data)

    coc_card.set("edu_expr", '["本:集美大学", "硕: 密斯卡托尼克大学"]')
    assert coc_card.get("edu_expr") == ["本:集美大学", "硕: 密斯卡托尼克大学"]

    coc_card.set("job", ["医生", "间谍"])
    coc_card.set("职业", ["医生", "间谍"])
    assert coc_card.get("edu_expr") == coc_card.get("学历")

    coc_card.set("学历", '["本:集美大学", "硕: 密斯卡托尼克大学"]')
    assert coc_card.get("学历") == ["本:集美大学", "硕: 密斯卡托尼克大学"]

    coc_card.set("test", "+4.0")
    assert coc_card.get("test") == 5

    assert coc_card.get_by_group_name("技能") == {"侦查": 50}
    assert coc_card.get_by_group_name("个人信息") == {
        "sex": "男",
        "age": 22,
        "edu_expr": ["本:集美大学", "硕: 密斯卡托尼克大学"],
        "job": ["医生", "间谍"],
    }

    coc_card.set("b", "+4.0")
    coc_card.set("b", "+3")
    coc_card.set("b", "-1")
    assert coc_card.get("b") == 6
