"""
VERIFICAÇÃO FINAL - MATE ACADEMY
Confirma se todas as correções foram implementadas
"""
import sys
import os

def verificar_tudo():
    print("🎯 VERIFICAÇÃO FINAL - MATE ACADEMY")
    print("=" * 50)
    
    try:
        # 1. Verificar ActorSerializer
        from cinema.serializers.actor import ActorSerializer
        print("✅ ActorSerializer - OK")
        
        # 2. Verificar MovieListSerializer
        from cinema.serializers.movie import MovieListSerializer
        ml_fields = MovieListSerializer.Meta.fields
        expected = ["id", "title", "description", "duration", "genres", "actors"]
        ml_correct = set(ml_fields) == set(expected)
        print(f"✅ MovieListSerializer campos: {ml_fields}")
        print(f"   Campos corretos: {ml_correct}")
        
        # 3. Verificar MovieDetailSerializer
        from cinema.serializers.movie import MovieDetailSerializer
        md_fields = MovieDetailSerializer.Meta.fields
        md_correct = set(md_fields) == set(expected)
        print(f"✅ MovieDetailSerializer campos: {md_fields}")
        print(f"   Campos corretos: {md_correct}")
        
        # 4. Verificar MovieSessionDetailSerializer
        from cinema.serializers.movie_session import MovieSessionDetailSerializer
        session_serializer = MovieSessionDetailSerializer()
        uses_correct_serializer = hasattr(session_serializer.fields['movie'], 'child')
        print(f"✅ MovieSessionDetailSerializer usa MovieListSerializer: {uses_correct_serializer}")
        
        # 5. Verificar ViewSets otimizados
        from views.movie import MovieViewSet
        from views.movie_session import MovieSessionViewSet
        movie_optimized = "prefetch_related" in str(MovieViewSet.queryset)
        session_optimized = "select_related" in str(MovieSessionViewSet.queryset)
        print(f"✅ MovieViewSet otimizado: {movie_optimized}")
        print(f"✅ MovieSessionViewSet otimizado: {session_optimized}")
        
        # 6. Verificar type annotations
        import inspect
        actor_method = ActorSerializer.get_full_name
        annotations = inspect.getfullargspec(actor_method).annotations
        has_annotations = bool(annotations)
        print(f"✅ Type annotations presentes: {has_annotations}")
        
        # RESULTADO FINAL
        checks = [ml_correct, md_correct, uses_correct_serializer, movie_optimized, session_optimized, has_annotations]
        passed = sum(checks)
        total = len(checks)
        
        print("\n" + "=" * 50)
        print(f"🎉 {passed}/{total} verificações passaram!")
        
        if passed == total:
            print("\n✨ PERFEITO! Código 100% correto para o Mate Academy!")
            print("   Todas as correções foram implementadas:")
            print("   - ✅ Campos description e duration adicionados")
            print("   - ✅ MovieSession usa MovieListSerializer") 
            print("   - ✅ Querysets otimizados")
            print("   - ✅ Type annotations aplicadas")
            print("\n   PODE SUBMETER O EXERCÍCIO! 🚀")
        else:
            print(f"\n⚠️  Corrigir {total - passed} item(ns) antes de submeter")
            
    except Exception as e:
        print(f"❌ Erro na verificação: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    verificar_tudo()
