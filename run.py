from omegaconf import DictConfig
import hydra
import zhei as j

log = j.Logger(__name__)

@hydra.main(version_base="1.2", config_path="configs/", config_name="default_config.yaml")
def main(config: DictConfig) -> float:
    j.hi()
    j.help()
    config = j.init_env(config)
    # ---------------------------------------------------------------------------- #
    #                          加载数据集                                    
    # ---------------------------------------------------------------------------- #
    # dataset = load_dataset("cais/mmlu", "high_school_geography")
    # dataset.push_to_hub("cais/mmlu", "high_school_geography")
    
    # tokenizer = LlamaTokenizer.from_pretrained("chainyo/alpaca-lora-7b")
    # tokenizer.add_special_tokens({'pad_token': '[PAD]'})
    
    # columns_map = {
    #     "input_ids": "question",
    #     "labels": "answer",
    # }
    # dataset = j.advance_tokenize(tokenizer, dataset, columns_map, truncation=True, padding=True)
    
    # ---------------------------------------------------------------------------- #
    #                         加载模型                                     
    # ---------------------------------------------------------------------------- #
    
    
    
    # ---------------------------------------------------------------------------- #
    #                         算力准备                                     
    # ---------------------------------------------------------------------------- #
    config = j.set_processing_units(config)
    
    
    # ---------------------------------------------------------------------------- #
    #                         模型训练                                     
    # ---------------------------------------------------------------------------- #
    
    
    
    
    # ---------------------------------------------------------------------------- #
    #                         模型预测                                               
    # ---------------------------------------------------------------------------- #

        
        
    # ---------------------------------------------------------------------------- #
    #                         结果评价                                     
    # ---------------------------------------------------------------------------- #
    
    
    
    
    # ---------------------------------------------------------------------------- #
    #                         结果可视化、保存                                     
    # ---------------------------------------------------------------------------- #    
    
    print()

    
    
    
if __name__ == "__main__":
    main()