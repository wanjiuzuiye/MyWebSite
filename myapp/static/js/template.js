(function($) {
  'use strict';
  $(function() {
    var body = $('body');
    var contentWrapper = $('.content-wrapper');
    var scroller = $('.container-scroller');
    var footer = $('.footer');
    var sidebar = $('.sidebar');

    //Add active class to nav-link based on url dynamically
    //Active class can be hard coded directly in html file also as required
    function addActiveClass(element) {
      // 获取当前页面路径的最后一部分
      var current = location.pathname.split('/').filter(Boolean).pop() || '';
    
      // 去掉查询参数进行比较
      var href = element.attr('href').split('?')[0]; 
    
      if (current === '' && href.indexOf('index.html') !== -1) {
        // 根路径或首页
        element.parents('.nav-item').last().addClass('active');
        if (element.parents('.sub-menu').length) {
          element.closest('.collapse').addClass('show'); // 展开子菜单
          element.addClass('active');
        }
      } else if (href.indexOf(current) !== -1) {
        // 其他页面
        element.parents('.nav-item').last().addClass('active');
        if (element.parents('.sub-menu').length) {
          element.closest('.collapse').addClass('show');
          element.addClass('active');
        }
        if (element.parents('.submenu-item').length) {
          element.addClass('active');
        }
      }
    }
    
    // 确保文档加载完毕后执行
    $(document).ready(function() {
      // 遍历 sidebar 中的每个 <a> 元素，应用 active 类
      $('.nav li a').each(function() {
        var $this = $(this);
        addActiveClass($this);
      });
    });

    //Close other submenu in sidebar on opening any

    sidebar.on('show.bs.collapse', '.collapse', function() {
      sidebar.find('.collapse.show').collapse('hide');
    });


    //Change sidebar

    $('[data-toggle="minimize"]').on("click", function() {
      body.toggleClass('sidebar-icon-only');
    });

    //checkbox and radios
    $(".form-check label,.form-radio label").append('<i class="input-helper"></i>');
   

  });



})(jQuery);