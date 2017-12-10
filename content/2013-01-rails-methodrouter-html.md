Title: \[Rails\] 新しく追加したmethodのrouter設定
Date: 2013-01-04 22:03
Authors: ayakomuro
Tags:  Rails
Slug:2013/01/rails-methodrouter
Status: published

通常のscaffoldだと


     
    class ProjectsController < ApplicationController 
      def index
      def edit
      def new
      def show
      def delete

のmethodが追加されるが、新しくmethod追加された場合

     
    class ProjectsController < ApplicationController 
      def summary #新しく追加した

config/router.rbに追加してあげる必要がある

     
    WebTest::Application.routes.draw do
      resources :projects do
        collection do                                                                                                                         
          get 'summary'
        end
      end

これだと/projects/summaryとして使える
特定のレコードに対して新たに処理を追加したい場合はこうする

    WebTest::Application.routes.draw do
      resources :projects do
        member do                                                                                                                         
          get 'summary'
        end
      end

こうすると/projects/1/summaryとして使える
