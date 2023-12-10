// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]
use rtrend::{Client, Country, Keywords, SearchInterest};
use serde_json::Number;

fn get_metric_for_keyword(keyword: &str) -> u64 {
    let keywords: &'static str = String::from(keyword.split(" ").collect::<Vec<&str>>()[0]).leak();
    let client = Client::new(Keywords::from(keywords), Country::ALL).build();

    let search_interest = SearchInterest::new(client).get();
    let metric = search_interest["default"]["timelineData"]
        .as_array()
        .unwrap()
        .last()
        .unwrap()
        .get("value")
        .unwrap()[0]
        .as_u64()
        .unwrap();

    metric
}

// Learn more about Tauri commands at https://tauri.app/v1/guides/features/command
#[tauri::command]
fn get_best(first_thing: &str, second_thing: &str) -> Number {
    let first_rank = get_metric_for_keyword(first_thing);
    let second_rank = get_metric_for_keyword(second_thing);

    if first_rank > second_rank {
        Number::from(1)
    } else {
        Number::from(2)
    }
}

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![get_best])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
