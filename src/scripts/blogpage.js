(function() {
  const blogs_container = document.getElementById("blog__blog-cards");

  const blog_card_template = _.template(`
  <div class="blog-card">
  <div class="blog-card__blog-card-header">
    <div class="blog-card__blog-card-header__avatar"></div>
    <div class="blog_card__blog-card-header__username">
      <h4 class="font-subtitle"><a href="#">Ирина Кибина</a></h4>
      <p class="font-text-sm">12 марта 2019</p>
    </div>
  </div>
  <div class="blog-card__blog-card-body">
    <h4 class="font-title-sm">
      <a href="./publication.html"
        > <%= title %> </a>
        </h4>
        <p class="font-text">
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Amet
      facere, sequi nihil reiciendis magni deleniti?Lorem ipsum
      dolor sit amet consectetur adipisicing elit. Ex dolorem
      laboriosam saepe eligendi iure totam corrupti, voluptates
      natus. Neque, eligendi!
        </p>
        <div class="blog-card__blog-card-body__img"></div>
    </div>
    </div>
  `);

  const requestBlogPosts = () => {
    return axios
      .get("https://jsonplaceholder.typicode.com/posts")
      .then(response => {
        return response.data;
      })
      .catch(error => {
        console.error(error);
      });
  };

  const renderBlogPost = posts => {
    posts.map(p);
  };
})();
