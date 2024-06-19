"""
Convenience script(s) to
Retrieve assets (cards, mutators, clans, heroes) ids from the -previously downloaded, "constants"

- Leaderboard API responses return lot of ids (for cards, mutators, relics...)
- Modding community already parsed the assets.
- See. https://github.com/brandonandzeus/Trainworks2
- Specifically in /ConstantsV2 folder : .cs files that we will parse into a single file.
- We already downloaded the .cs files in utils/ (cf. dl_constants.py)
"""

# retained format

json_db_example = {
    "clan": {
        "c595c344-d323-4cf1-9ad6-41edc2aebbd0": {
            "from_file": "VanillaClanIDs",
            "asset_name": "classHellhorned",
            "asset_string": "Hellhorned",
        }
    },
    "card": {
        "b987c567-d123-4cf1-9abc-12edc3aef123": {
            "from_file": "VanillaCardIDs",
            "asset_name": "cardExample",
            "asset_string": "ExampleCard",
        }
    },
    "mutator": {
        "a123c789-d456-4cf1-9xyz-34edc5efgh45": {
            "from_file": "VanillaMutatorIDs",
            "asset_name": "mutatorExample",
            "asset_string": "ExampleMutator",
        }
    },
}

# retained format for separate files. E.g clanIds
filename = "VanillaClanIDs.cs"
{
    "c595c344-d323-4cf1-9ad6-41edc2aebbd0": {
        "from_file": "VanillaClanIDs",
        "asset_name": "classHellhorned",
        "asset_string": "Hellhorned",
    },
    "fd119fcf-c2cf-469e-8a5a-e9b0f265560d": {
        "from_file": "VanillaClanIDs",
        "asset_name": "ClassAwoken",
        "asset_string": "Awoken",
    },

}


"VanillaClanIDs.cs":"clan"
"VanillaCovenentIDs.cs":"covenant"
"VanillaMutatorIDs.cs":"mutator"
"VanillaCardIDs.cs":"card"
"VanillaCardUpgradeDataIDs.cs":"card_upgrade"
"VanillaRelicIDs.cs":"relic"
"VanillaCollectableRelicIDs.cs":"relic_collectable"
"VanillaTrialIDs.cs":"trial"
