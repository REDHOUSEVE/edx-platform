// Once generated by CoffeeScript 1.9.3, but now lives as pure JS
/* eslint-disable */
(function() {
  this.Conditional = (function() {
    function Conditional(element, callerElId) {
      var dependencies;
      this.el = $(element).find('.conditional-wrapper');
      this.callerElId = callerElId;
      if (callerElId !== void 0) {
        dependencies = this.el.data('depends');
        if ((typeof dependencies === 'string') && (dependencies.length > 0) && (dependencies.indexOf(callerElId) === -1)) {
          return;
        }
      }
      this.url = this.el.data('url');
      if (this.url) {
        this.render(element);
      }
    }

    Conditional.prototype.render = function(element) {
      return $.postWithPrefix(this.url + "/conditional_get", (function(_this) {
        return function(response) {
          var i, len, parentEl, parentId, ref, renderedFragments=[];
          _this.el.html('');
          fragments = response.fragments;
          for (i = 0, len = fragments.length; i < len; i++) {
            renderedFragments.push(_this.renderXBlockFragment(fragments[i]));
            console.log("Started fragment loading", fragments[i])
          }
          parentEl = $(element).parent();
          parentId = parentEl.attr('id');
          if (response.message === false) {
            if (parentEl.hasClass('vert')) {
              parentEl.hide();
            } else {
              $(element).hide();
            }
          } else {
            if (parentEl.hasClass('vert')) {
              parentEl.show();
            } else {
              $(element).show();
            }
          }

          /*
          The children are rendered with a new request, so they have a different request-token.
          Use that token instead of @requestToken by simply not passing a token into initializeBlocks.
          */
          $.when.apply(null, renderedFragments).done(function() {
              console.log("All fragments loaded, initializing blocks");
              XBlock.initializeBlocks(_this.el);
          });
        };
      })(this));
    };


    /**
    * Renders an xblock fragment into the specified element. The fragment has two attributes:
    *   html: the HTML to be rendered
    *   resources: any JavaScript or CSS resources that the HTML depends upon
    * Note that the XBlock is rendered asynchronously, and so a promise is returned that
    * represents this process.
    * @param fragment The fragment returned from the xblock_handler
    * @returns {Promise} A promise representing the rendering process
    */
    Conditional.prototype.renderXBlockFragment = function(fragment) {
      var html = fragment.content,
      resources = fragment.resources || [],
      element = this.el;
      // Render the HTML first as the scripts might depend upon it, and then
      // asynchronously add the resources to the page. Any errors that are thrown
      // by included scripts are logged to the console but are then ignored assuming
      // that at least the rendered HTML will be in place.
      try {
        return this.addXBlockFragmentResources(resources).done(function () {
          // We give XBlock fragments free-reign to add javascript and CSS to
          // to the page, so XSS escaping doesn't matter much in this context
          // xss-lint: disable=javascript-jquery-append
          console.log("Fragment resources loaded, appending HTML");
          element.append(html);
        });
      } catch (e) {
        console.error(e, e.stack);
        return $.Deferred().resolve();
      }
    };

    /**
    * Dynamically loads all of an XBlock's dependent resources. This is an asynchronous
    * process so a promise is returned.
    * @param resources The resources to be rendered
    * @returns {Promise} A promise representing the rendering process
    */
    Conditional.prototype.addXBlockFragmentResources = function(resources) {
      var self = this;
      var applyResource;
      var numResources;
      var deferred;
      var numResources = resources.length;
      var deferred = $.Deferred();

      applyResource = function (index) {
        var hash, resource, value, promise;
        if (index >= numResources) {
          deferred.resolve();
          return;
        }
        resource = resources[index];
        window.loadedXBlockResources = window.loadedXBlockResources || [];
        if (_.indexOf(loadedXBlockResources, resource) < 0) {
          promise = self.loadResource(resource);
          loadedXBlockResources.push(resource);
          promise.done(function () {
            applyResource(index + 1);
          }).fail(function () {
            deferred.reject();
          });
        } else {
          applyResource(index + 1);
        }
      };
      applyResource(0);
      return deferred.promise();
    };

    /**
    * Loads the specified resource into the page.
    * @param resource The resource to be loaded.
    * @returns {Promise} A promise representing the loading of the resource.
    */
    Conditional.prototype.loadResource = function(resource) {
      // We give XBlock fragments free-reign to add javascript and CSS to
      // to the page, so XSS escaping doesn't matter much in this context
      var $head = $('head'),
      mimetype = resource.mimetype,
      kind = resource.kind,
      placement = resource.placement,
      data = resource.data;
      if (mimetype === 'text/css') {
        if (kind === 'text') {
          // xss-lint: disable=javascript-jquery-append,javascript-concat-html
          $head.append("<style type='text/css'>" + data + '</style>');
        } else if (kind === 'url') {
          // xss-lint: disable=javascript-jquery-append,javascript-concat-html
          $head.append("<link rel='stylesheet' href='" + data + "' type='text/css'>");
        }
      } else if (mimetype === 'application/javascript') {
        if (kind === 'text') {
            $head.append('<script>' + data + '</script>');
        } else if (kind === 'url') {
          $script(data, data);
        }
      } else if (mimetype === 'text/html') {
        if (placement === 'head') {
          // xss-lint: disable=javascript-jquery-append
          $head.append(data);
        }
      }
      // Return an already resolved promise for synchronous updates
      return $.Deferred().resolve().promise();
    };

    return Conditional;

  })();

}).call(this);
