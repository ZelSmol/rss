async function get_news() {
    let value_url = document.getElementById("url-input").value;
    document.querySelector(".news-container").innerHTML = await eel.news_by_url(value_url)();

}

async function get_news_set() {
    document.querySelector(".news-container").innerHTML = await eel.get_news_set()();
}

document.getElementById("btn-get").onclick = get_news;
get_news_set();