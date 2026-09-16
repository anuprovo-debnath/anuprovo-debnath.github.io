// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "About",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-cv",
          title: "CV",
          description: "Academic curriculum vitae detailing my education, research interests, projects, and awards.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "nav-projects",
          title: "Projects",
          description: "Here are the projects I have been working on.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/projects/";
          },
        },{id: "nav-bookshelf",
          title: "Bookshelf",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/books/";
          },
        },{id: "nav-repositories",
          title: "Repositories",
          description: "Here are some of my favourite repositories.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/repositories/";
          },
        },{id: "books-1984",
          title: '1984',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/1984/";
            },},{id: "books-animal-farm",
          title: 'Animal Farm',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/animal_farm/";
            },},{id: "books-brave-new-world",
          title: 'Brave New World',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/brave_new_world/";
            },},{id: "books-catch-22",
          title: 'Catch-22',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/catch-22/";
            },},{id: "books-children-of-dune",
          title: 'Children of Dune',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/children_of_dune/";
            },},{id: "books-crime-and-punishment",
          title: 'Crime and Punishment',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/crime_and_punishment/";
            },},{id: "books-do-androids-dream-of-electric-sheep",
          title: 'Do Androids Dream of Electric Sheep?',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/do_androids_dream_of_electric_sheep/";
            },},{id: "books-dune",
          title: 'Dune',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/dune/";
            },},{id: "books-dune-messiah",
          title: 'Dune Messiah',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/dune_messiah/";
            },},{id: "books-fahrenheit-451",
          title: 'Fahrenheit 451',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/fahrenheit_451/";
            },},{id: "books-foundation",
          title: 'Foundation',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/foundation/";
            },},{id: "books-foundation-and-earth",
          title: 'Foundation and Earth',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/foundation_and_earth/";
            },},{id: "books-foundation-and-empire",
          title: 'Foundation and Empire',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/foundation_and_empire/";
            },},{id: "books-foundation-39-s-edge",
          title: 'Foundation&amp;#39;s Edge',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/foundations_edge/";
            },},{id: "books-notes-from-underground",
          title: 'Notes from Underground',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/notes_from_underground/";
            },},{id: "books-room-of-many-colours",
          title: 'Room of Many Colours',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/room_of_many_colours/";
            },},{id: "books-second-foundation",
          title: 'Second Foundation',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/second_foundation/";
            },},{id: "books-the-brothers-karamazov",
          title: 'The Brothers Karamazov',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/the_brothers_karamazov/";
            },},{id: "books-the-death-of-ivan-ilyich",
          title: 'The Death of Ivan Ilyich',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/the_death_of_ivan_ilyich/";
            },},{id: "books-war-and-peace",
          title: 'War and Peace',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/war_and_peace/";
            },},{id: "news-a-simple-inline-announcement",
          title: 'A simple inline announcement.',
          description: "",
          section: "News",},{id: "news-a-long-announcement-with-details",
          title: 'A long announcement with details',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/announcement_2/";
            },},{id: "news-a-simple-inline-announcement-with-markdown-emoji-sparkles-smile",
          title: 'A simple inline announcement with Markdown emoji! :sparkles: :smile:',
          description: "",
          section: "News",},{id: "projects-evaluating-plasma-parameters-from-a-typical-libs-plasma",
          title: 'Evaluating Plasma Parameters from a Typical LIBS Plasma',
          description: "Summer Internship Project at Physical Research Laboratory (PRL), Ahmedabad",
          section: "Projects",handler: () => {
              window.location.href = "/projects/libs_project/";
            },},{id: "projects-simulation-and-analysis-of-ns-dbd-plasma-actuator-shock-waves",
          title: 'Simulation and Analysis of ns-DBD Plasma Actuator Shock Waves',
          description: "IASc-INSA-NASI Summer Research Fellowship (SRFP) Project at CSIR-CMERI",
          section: "Projects",handler: () => {
              window.location.href = "/projects/ns-dbd_project/";
            },},{id: "teachings-data-science-fundamentals",
          title: 'Data Science Fundamentals',
          description: "This course covers the foundational aspects of data science, including data collection, cleaning, analysis, and visualization. Students will learn practical skills for working with real-world datasets.",
          section: "Teachings",handler: () => {
              window.location.href = "/teachings/data-science-fundamentals/";
            },},{id: "teachings-introduction-to-machine-learning",
          title: 'Introduction to Machine Learning',
          description: "This course provides an introduction to machine learning concepts, algorithms, and applications. Students will learn about supervised and unsupervised learning, model evaluation, and practical implementations.",
          section: "Teachings",handler: () => {
              window.location.href = "/teachings/introduction-to-machine-learning/";
            },},{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
